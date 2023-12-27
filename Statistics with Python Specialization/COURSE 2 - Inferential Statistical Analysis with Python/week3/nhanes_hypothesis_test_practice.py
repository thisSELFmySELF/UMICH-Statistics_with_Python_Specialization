
# coding: utf-8

# # Practice notebook for hypothesis tests using NHANES data
# 
# This notebook will give you the opportunity to perform some hypothesis tests with the NHANES data that are similar to
# what was done in the week 3 case study notebook.
# 
# You can enter your code into the cells that say "enter your code here", and you can type responses to the questions into the cells that say "Type Markdown and Latex".
# 
# Note that most of the code that you will need to write below is very similar to code that appears in the case study notebook.  You will need to edit code from that notebook in small ways to adapt it to the prompts below.
# 
# To get started, we will use the same module imports and read the data in the same way as we did in the case study:

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats.distributions as dist
from statsmodels.stats.proportion import proportion_confint

da = pd.read_csv("nhanes_2015_2016.csv")


# ## Question 1
# 
# Conduct a hypothesis test (at the 0.05 level) for the null hypothesis that the proportion of women who smoke is equal to the proportion of men who smoke.

# In[2]:


# insert your code here

da_male_smoke = da[da['RIAGENDR']==1]['SMQ020']
da_male_smoke = da_male_smoke[~da_male_smoke.isna()]
da_male_smoke.reset_index(inplace = True, drop = True)

da_female_smoke = da[da['RIAGENDR'] == 2]['SMQ020']
da_female_smoke = da_female_smoke[~da_female_smoke.isna()]
da_female_smoke.reset_index(inplace = True, drop = True)


# In[3]:


print(sum(da_male_smoke == 1), ",", sum(da_male_smoke != 1))


# In[4]:


print(sum(da_female_smoke == 1), ",", sum(da_female_smoke != 1))


# In[5]:


sum(da_male_smoke == 1) / len(da_male_smoke)


# In[6]:


sum(da_female_smoke == 1) / len(da_female_smoke)


# In[7]:


(np.std(da_male_smoke) ** 2) / (np.std(da_female_smoke) ** 2)


# In[8]:


sm.stats.ttest_ind(da_male_smoke, da_female_smoke)


# In[9]:


ci_low, ci_upp = proportion_confint(sum(da_female_smoke == 1), len(da_female_smoke), alpha = 0.05, method = 'normal')
ci_low, ci_upp


# In[10]:


ci_low, ci_upp = proportion_confint(sum(da_male_smoke == 1), len(da_male_smoke), alpha = 0.05, method = 'normal')
ci_low, ci_upp


# In[11]:


proportion_male_smokers = (sum(da_male_smoke == 1) / len(da_male_smoke))
proportion_male_smokers


# In[12]:


proportion_female_smokers = (sum(da_female_smoke == 1) / len(da_female_smoke))
proportion_female_smokers


# In[13]:


proportion_smokers_gender_diff = proportion_male_smokers - proportion_female_smokers
proportion_smokers_gender_diff


# In[14]:


se_smokers_gender_male = np.sqrt((proportion_male_smokers * (1 - proportion_male_smokers)) / len(da_male_smoke))
se_smokers_gender_male


# In[15]:


se_smokers_gender_female = np.sqrt((proportion_female_smokers * (1 - proportion_female_smokers)) / len(da_female_smoke))
se_smokers_gender_female


# In[16]:


se_proportion_smokers_diff = np.sqrt((se_smokers_gender_male ** 2) + (se_smokers_gender_female ** 2))
se_proportion_smokers_diff


# In[17]:


print('Lower Boundary Male: ', proportion_smokers_gender_diff - 1.96 * se_proportion_smokers_diff)
print('Upper Boundary Male: ', proportion_smokers_gender_diff + 1.96 * se_proportion_smokers_diff)


# __Q1a.__ Write 1-2 sentences explaining the substance of your findings to someone who does not know anything about statistical hypothesis tests.

# __Q1b.__ Construct three 95% confidence intervals: one for the proportion of women who smoke, one for the proportion of men who smoke, and one for the difference in the rates of smoking between women and men.

# In[18]:


# insert your code here


# __Q1c.__ Comment on any ways in which the confidence intervals that you found in part b reinforce, contradict, or add support to the hypothesis test conducted in part a.

# The confidence intervals support our conclusion that the the proportion of males who smoke is significant from the proportion of females who smoke. The confidence interval for the proportion of males who smoke does not overlap with the proportion of females who smoke. The confidence interval for the difference between the two proportions does not include zero.

# ## Question 2
# 
# Partition the population into two groups based on whether a person has graduated college or not, using the educational attainment variable [DMDEDUC2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDEDUC2).  Then conduct a test of the null hypothesis that the average heights (in centimeters) of the two groups are equal.  Next, convert the heights from centimeters to inches, and conduct a test of the null hypothesis that the average heights (in inches) of the two groups are equal.

# In[19]:


# insert your code here

da_graduated_height_cm = da[da['DMDEDUC2'] == 5]['BMXHT']
da_graduated_height_cm = da_graduated_height_cm[~da_graduated_height_cm.isna()]
da_graduated_height_cm.reset_index(inplace = True, drop = True)
da_not_graduated_height_cm=da[da['DMDEDUC2'] != 5]['BMXHT']
da_not_graduated_height_cm = da_not_graduated_height_cm[~da_not_graduated_height_cm.isna()]
da_not_graduated_height_cm.reset_index(inplace=True, drop = True)


# In[20]:


len(da_graduated_height_cm)


# In[21]:


len(da_not_graduated_height_cm)


# In[22]:


da_graduated_height_cm.mean()


# In[23]:


da_not_graduated_height_cm.mean()


# In[24]:


print(sm.stats.ztest(da_graduated_height_cm, da_not_graduated_height_cm))


# In[25]:


da_graduated_height_inches = da_graduated_height_cm / 2.54
da_graduated_height_inches = da_graduated_height_inches[~da_graduated_height_inches.isna()]
da_graduated_height_inches.reset_index(inplace = True, drop = True)


# In[26]:


da_not_graduated_height_inches = da_not_graduated_height_cm / 2.54
da_not_graduated_height_inches= da_not_graduated_height_inches[~da_not_graduated_height_inches.isna()]
da_not_graduated_height_inches.reset_index(inplace = True, drop = True)


# In[27]:


print(sm.stats.ztest(da_graduated_height_inches, da_not_graduated_height_inches))


# __Q2a.__ Based on the analysis performed here, are you confident that people who graduated from college have a different average height compared to people who did not graduate from college?

# Yes. The p-value is very small which means that we should reject the null hypothesis in favor of the alternative one.

# __Q2b:__ How do the results obtained using the heights expressed in inches compare to the results obtained using the heights expressed in centimeters?

# The z-statistic and p-values are very similar.

# ## Question 3
# 
# Conduct a hypothesis test of the null hypothesis that the average BMI for men between 30 and 40 is equal to the average BMI for men between 50 and 60.  Then carry out this test again after log transforming the BMI values.

# In[28]:


# insert your code here

da_bmi = da[(da['RIDAGEYR'] >= 30) & (da['RIDAGEYR'] <= 40)]
da_bmi.reset_index(inplace = True, drop = True)


# In[29]:


bmi_men = da_bmi[da_bmi['RIAGENDR'] == 1]['BMXBMI']
bmi_men = bmi_men[~bmi_men.isna()]
bmi_men.reset_index(inplace = True, drop = True)


# In[30]:


bmi_women = da_bmi[da_bmi['RIAGENDR'] == 2]['BMXBMI']
bmi_women = bmi_women[~bmi_women.isna()]
bmi_women.reset_index(inplace = True, drop = True)


# In[31]:


len(bmi_men)


# In[32]:


len(bmi_women)


# In[33]:


print(sm.stats.ztest(bmi_men, bmi_women))


# In[34]:


bmi_men_log = np.log(bmi_men)


# In[35]:


bmi_women_log = np.log(bmi_women)


# In[36]:


print(sm.stats.ztest(bmi_men_log, bmi_women_log))


# __Q3a.__ How would you characterize the evidence that mean BMI differs between these age bands, and how would you characterize the evidence that mean log BMI differs between these age bands?

# In both, the mean BMI does not significally differ between the two genders. The p-value is higher after applying log transform to our values. Therefore, we fail to reject the null hypothesis.

# ## Question 4
# 
# Suppose we wish to compare the mean BMI between college graduates and people who have not graduated from college, focusing on women between the ages of 30 and 40.  First, consider the variance of BMI within each of these subpopulations using graphical techniques, and through the estimated subpopulation variances.  Then, calculate pooled and unpooled estimates of the standard error for the difference between the mean BMI in the two populations being compared.  Finally, test the null hypothesis that the two population means are equal, using each of the two different standard errors.

# In[37]:


# insert your code here

da_bmi_women = da_bmi[da_bmi['RIAGENDR'] == 2]
da_bmi_women.reset_index(inplace = True, drop = True)

bmi_women_graduated = da_bmi_women[da_bmi_women['DMDEDUC2']==5]['BMXBMI']
bmi_women_graduated = bmi_women_graduated[~bmi_women_graduated.isna()]
bmi_women_graduated.reset_index(inplace = True, drop = True)

bmi_women_not_graduated = da_bmi_women[da_bmi_women['DMDEDUC2'].isin([1, 2, 3, 4])]['BMXBMI']
bmi_women_not_graduated = bmi_women_not_graduated[~bmi_women_not_graduated.isna()]
bmi_women_not_graduated.reset_index(inplace=True, drop = True)


# In[38]:


bmi_women_graduated.describe()


# In[39]:


bmi_women_not_graduated.describe()


# In[40]:


sns.boxplot(bmi_women_graduated)


# In[41]:


sns.boxplot(bmi_women_not_graduated)


# In[42]:


(np.std(bmi_women_graduated) ** 2) / (np.std(bmi_women_not_graduated) ** 2)


# In[43]:


bmi_women_graduated = sm.stats.DescrStatsW(bmi_women_graduated)
bmi_women_not_graduated = sm.stats.DescrStatsW(bmi_women_not_graduated)
print("pooled: ", sm.stats.CompareMeans(bmi_women_graduated, bmi_women_not_graduated).ztest_ind(usevar = 'pooled'))
print("unequal:", sm.stats.CompareMeans(bmi_women_graduated, bmi_women_not_graduated).ztest_ind(usevar = 'unequal'))


# __Q4a.__ Comment on the strength of evidence against the null hypothesis that these two populations have equal mean BMI.

# The two populations don't have an equal BMI and we will reject the null hypothesis since the p-value is really small and below our significant level for the alternative hypothesis.

# __Q4b.__ Comment on the degree to which the two populations have different variances, and on the extent to which the results using different approaches to estimating the standard error of the mean difference give divergent results.

# The variance difference between the two populations is not that huge therefore, the two approaches result in very close values and we reach the same conclusion.

# ## Question 5
# 
# Conduct a test of the null hypothesis that the first and second diastolic blood pressure measurements within a subject have the same mean values.

# In[44]:


# insert your code here

dx = da[["BPXDI1", "BPXDI2"]].dropna()
db = dx.BPXDI1 - dx.BPXDI2
print(db.mean())
sm.stats.ztest(db)


# __Q5a.__ Briefly describe your findings for an audience that is not familiar with statistical hypothesis testing.

# The first diastolic blood pressure is significally different from the second diastolic blood pressure.

# __Q5b.__ Pretend that the first and second diastolic blood pressure measurements were taken on different people.  Modfify the analysis above as appropriate for this setting.

# In[45]:


# insert your code here

BPXDI1 = da[~da['BPXDI1'].isna()]['BPXDI1']
BPXDI1.reset_index(inplace = True, drop = True)
BPXDI2 = da[~da['BPXDI2'].isna()]['BPXDI2']
BPXDI2.reset_index(inplace = True, drop = True)


# In[46]:


BPXDI1 = sm.stats.DescrStatsW(BPXDI1)
BPXDI2 = sm.stats.DescrStatsW(BPXDI2)
print(sm.stats.CompareMeans(BPXDI1, BPXDI2).ztest_ind(usevar='pooled'))


# __Q5c.__ Briefly describe how the approaches used and the results obtained in the preceeding two parts of the question differ.

# When treating the two measurments as unpaired and as separate individuals, we failed to reject the null hypothesis and the p-value was large but when treating the two measurments as paired and matched individuals, we rejected the null hypothesis as the p-value was below our significance leve.
