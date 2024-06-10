#!/usr/bin/env python3
#0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import abline_plot
import statsmodels.genmod
import statsmodels.genmod.families

#1
def get_path(filename):
    import sys
    import os
    prog_name = sys.argv[0]
    if os.path.basename(prog_name) == "__main__.py":   # Running under TMC
        return os.path.join(os.path.dirname(prog_name), "..", "src", filename)
    else:
        return filename

#2
def rescale(s):
    centered_data = s - s.mean()
    normalize_data = centered_data / (2 * s.std())
    return normalize_data

def logistic(x):
    return 1.0 / (1.0 + np.exp(-x))

#12
def train_test_split(df, train_fraction=0.8):
    train = df.sample(frac=train_fraction)
    test = df.drop(train.index)
    return train, test

def regression():
    #1
    # fram = pd.read_csv(get_path('fram.txt'), sep='\t')
    fram = pd.read_csv('src/fram.txt', sep='\t')
    # print(fram.describe())

    #3
    for col in fram.columns:
        if fram[col].dtype in ['float64', 'int64'] and col[0] != 's':
            fram["s"+col] = rescale(fram[col])
    # print(fram.columns)

    #4
    fit = smf.ols('SBP ~ sFRW + SEX + sCHOL', data=fram).fit()
    # fit.summary()

    #5
    fit = smf.ols('SBP ~ sFRW + SEX + sCHOL + sAGE', data=fram).fit()
    fit.summary()

    #6
    fit = smf.ols('SBP ~ sFRW + SEX + sCHOL + sAGE + sFRW:SEX + sFRW:sCHOL + sFRW:sAGE + SEX:sCHOL + SEX:sAGE + sCHOL:sAGE', data=fram).fit()

    #7
    p = fit.params
    fram[fram.SEX=="female"].plot.scatter("sFRW", "SBP")
    abline_plot(intercept=p.Intercept - p["sAGE"], slope=p.sFRW - p["sFRW:sAGE"], ax=plt.gca(), color="blue", label="youngest")
    abline_plot(intercept=p.Intercept, slope=p.sFRW, ax=plt.gca(), color="magenta", label="middle aged")
    abline_plot(intercept=p.Intercept + p["sAGE"], slope=p.sFRW + p["sFRW:sAGE"], ax=plt.gca(), color="red", label="oldest")
    # plt.grid()
    plt.legend()

    #8
    fit = smf.ols('SBP ~ sFRW + SEX + sCHOL + sAGE + sFRW:SEX + sFRW:sCHOL + sFRW:sAGE + SEX:sCHOL + SEX:sAGE + sCHOL:sAGE + sCIG + sFRW:sCIG + SEX:sCIG + sCHOL:sCIG + sAGE:sCIG', 
              data=fram).fit()
    p = fit.params
    fram[fram.SEX=="female"].plot.scatter("sCHOL", "SBP")
    abline_plot(intercept=p.Intercept - p["sCHOL"], slope=p.sFRW - p["sFRW:sCHOL"], ax=plt.gca(), color="blue", label="small")
    abline_plot(intercept=p.Intercept, slope=p.sFRW, ax=plt.gca(), color="magenta", label="average")
    abline_plot(intercept=p.Intercept + p["sCHOL"], slope=p.sFRW + p["sFRW:sCHOL"], ax=plt.gca(), color="red", label="large")
    plt.legend()

    #9
    fram["HIGH_BP"] = (fram.SBP >= 140) | (fram.DBP >= 90)
    # fram.HIGH_BP.head()
    # fram.HIGH_BP.value_counts()
    # fram.HIGH_BP = fram.HIGH_BP.map(int)
    fram['HIGH_BP'] = fram['HIGH_BP'].astype(int)
    # fram.HIGH_BP.head()
    # fram.HIGH_BP.mean()
    # fram.head()
    fit = smf.glm(formula="HIGH_BP ~ sFRW + SEX + SEX:sFRW", data=fram, family=sm.families.Binomial()).fit()
    # fit.summary()
    error_rate_orig = np.mean(((fit.fittedvalues < 0.5) & fram.HIGH_BP) | ((fit.fittedvalues > 0.5) & ~fram.HIGH_BP))
    # print(error_rate_orig)

    #10
    fit = smf.glm(formula="HIGH_BP ~ sFRW + SEX + SEX:sFRW + sAGE + sFRW:sAGE + SEX:sAGE", data=fram, family=sm.families.Binomial()).fit()
    error_rate = np.mean(((fit.fittedvalues < 0.5) & fram.HIGH_BP) | ((fit.fittedvalues > 0.5) & ~fram.HIGH_BP))
    # print(error_rate)
    print(error_rate_orig - error_rate)

    #11
    p = fit.params
    fig, ax = plt.subplots(1, 2, subplot_kw={"xlabel": "sFRW", "ylabel": "HIGH_BP"}, figsize=(14, 4))
    X=np.linspace(-2, 4, 100)
    ax[0].scatter(fram[fram.SEX == "female"].sFRW, fram[fram.SEX == "female"].HIGH_BP, color='blue', label='Data', marker="d")
    ax[0].plot(X, logistic(X*(p.sFRW - p["sFRW:sAGE"]) + (p.Intercept - p.sAGE)), color="blue", label="young")
    ax[0].plot(X, logistic(X*p.sFRW + p.Intercept), color="magenta", label="middle aged")
    ax[0].plot(X, logistic(X*(p.sFRW + p["sFRW:sAGE"]) + (p.Intercept + p.sAGE)), color="red", label="oldest")
    ax[0].legend()
    ax[1].scatter(fram[fram.SEX == "male"].sFRW, fram[fram.SEX == "male"].HIGH_BP, color='blue', label='Data', marker="d")
    ax[1].plot(X, logistic(X*(p.sFRW - p["sFRW:sAGE"] + p["SEX[T.male]:sFRW"]) + (p.Intercept - p.sAGE + p["SEX[T.male]"])), color="blue", label="young")
    ax[1].plot(X, logistic(X*(p.sFRW + p["SEX[T.male]:sFRW"]) + p["SEX[T.male]"] + p.Intercept), color="magenta", label="middle aged")
    ax[1].plot(X, logistic(X*(p.sFRW + p["sFRW:sAGE"] + p["SEX[T.male]:sFRW"]) + (p.Intercept + p.sAGE + p["SEX[T.male]"])), color="red", label="oldest")
    ax[1].legend()

    #13
    np.random.seed(1)
    error_model=[]
    for i in range(100):
        train, test = train_test_split(fram)
        fit = smf.glm(formula="HIGH_BP ~ sFRW + SEX + SEX:sFRW + sAGE + sFRW:sAGE + SEX:sAGE", 
                    data=train, family=sm.families.Binomial(statsmodels.genmod.families.links.Logit())).fit()
        pred = fit.predict(test, transform=True)
        error_rate = np.mean(((pred < 0.5) & (test.HIGH_BP == 1)) | ((pred > 0.5) & (test.HIGH_BP == 0)))
        error_model.append(error_rate)
    pd.Series(error_model).mean()

    #14
    fram["hasCHD"] = (fram["CHD"] > 0).astype(int)
    print(fram["hasCHD"].mean())

    #15
    fit = smf.glm(formula="hasCHD ~ sCHOL + sCIG + sFRW + sCHOL:sCIG + sCHOL:sFRW + sCIG:sFRW", 
              data=fram, family=sm.families.Binomial(statsmodels.genmod.families.links.Logit())).fit()
    error_rate = np.mean(((fit.fittedvalues < 0.5) & fram.hasCHD) | ((fit.fittedvalues > 0.5) & ~fram.hasCHD))
    error_rate

    #16
    p = fit.params
    X = np.linspace(-2, 4, 100)
    plt.scatter(fram.sFRW, fram.hasCHD, marker="d", color='blue')
    plt.plot(X, logistic(X * p.sFRW + p.Intercept), color='red')
    plt.xlabel('sFRW')
    plt.ylabel('hasCHD')

    #17
    new_fram = pd.read_csv('src/fram.txt', sep='\t')
    point = {'CHOL': [200], 'CIG': [17], 'FRW': [100]}
    new_fram = pd.concat([new_fram, pd.DataFrame(point)], ignore_index=True)
    for col in new_fram.columns:
        if new_fram[col].dtype in ['float64', 'int64'] and col[0] != 's':
            new_fram["s" + col] = rescale(new_fram[col])
    '''new_fram["sFRW"] = rescale(new_fram.FRW)
    new_fram["sCHOL"] = rescale(new_fram.CHOL)
    new_fram["sCIG"] = rescale(new_fram.CIG)'''
    new_fram["hasCHD"] = (new_fram["CHD"] > 0).astype(int)
    point = {'sCHOL': new_fram['sCHOL'].iloc[-1], 'sCIG': new_fram['sCIG'].iloc[-1], 'sFRW': new_fram['sFRW'].iloc[-1]}
    fit = smf.glm(formula="hasCHD ~ sCHOL + sCIG + sFRW + sCHOL:sCIG + sCHOL:sFRW + sCIG:sFRW", 
                data=fram, family=sm.families.Binomial(statsmodels.genmod.families.links.Logit())).fit()
    predicted = fit.predict(point, transform=True)[0]
    print(predicted)

    plt.show()
    
def main():
    regression()

if __name__ == "__main__":
    main()