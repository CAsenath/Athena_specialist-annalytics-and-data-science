#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


loans=pd.read_csv("kiva_loans.csv.zip")


# In[4]:


#loans


# In[5]:


theme_ids=pd.read_csv("loan_theme_ids.csv.zip")


# In[6]:


#theme_ids


# In[7]:


themes_region=pd.read_csv("loan_themes_by_region.csv.zip")


# In[8]:


#themes_region


# In[9]:


region_locations=pd.read_csv("kiva_mpi_region_locations.csv")


# In[10]:


#region_locations


# Question 1
# 
# Define 2-3 metrics that can be generated using the existing datasets. Explain why you've chosen each metric and the pros and cons of their usage.

# METRICS
# This is my finding on the business metrics measures that will improve the Kiva’s performance.
# 
# 1.	CUSTOMER LOYALTY RETENTION
# Retention rate is shown by the number of loan clients who keep retaking the Kiva loan over an extended time period making repeat borrowing. This here has been exhited by most clients being depicted by the unique partner_id. A higher customer retention means potential profitability to Kiva, and can also help in determining how much can be used to invest in customer acquisition.
# 
# Metrics uses quantitative measures to track and monitor the success of any business model. In this case funded_amount if the most ideal to depict this.
# 
# PROS: 
# 1.	It easily shows our strongholds and successes.
# 2.	Positive comments from the return clients helps the firm in marketing itself.
# 3.	You can use the findings from the data to know where to improve on
# 4.	Easy to map out regions where not performing well
# 
# CONS:
# 1.	Limits the clientele scope to only existing clients
# 2.	Limits the potential of knowing the existence of other new clients.
# 
# 
# 2.LOANS GROWTH RATE
# This is a measure that shows how a company is increasing or decreasing.Various months depending on the seasons will perform differently. Long term tracking of the trends will better gadge the performance of a company.
# This can be achieved by calculating monthly loans and the number of new clients who come in board sekking for loans. The use of regions in our case will help us tom know who is more in need of our funding since Kiva is majorly for funding the poor.
# 
# PROS:
#     1. Easy to predict for the subsequent months when more funds will be needed.
#     2. The trends makes it easy to allocate funds
#     3. Easy to tell the best performing months\seasons and years.
#     
#  CONS:
#         1. Time\season is not the only measure that can be used to determine the success or failure of an organisation.
#         
#         
#     
#     
#     

# Question 2
# 
# Perform a short analysis on 1 of your defined metrics

# In[20]:


loans.plot(kind='scatter',x='partner_id',y='funded_amount',figsize=(6,6))


# I have illustrated using Customer Loyalty retention metrics.
# 
# This shows the relationship between partner_id and funded_amount.You can tell that the return clients were given more loans than new clients.

# Question 3.
# 
# Provide a detailed recommendation for tracking and reporting on your defined metrics. Suggest specific tools or methodologies. Additionally, outline any potential challenges that may arise, such as data quality issues.

# 1. Make it understable: This is achieved by limiting the number of metric plans to use. In our case i have majored on two that is, Customer loyalty retention and Loan growth rate. 
#     
#     Also using readable font is key reporting .
#     
#     I have also used a graph for easy understanding.
#     
# 2. Relevance of the metrics: Kiva deals with loans and majorly funding the poor , hence i have tailored my findings to that.
#     
#     
#     Tools or methodologies to use
#     
#  1. Dashboards:  this can be easily customised to display data to clients that can be easily understood and it makes it easy to relate.
#     
#     Google annalytics: this gives indepth to many metrics that you can use.
#         
#         Challenges:
#             
#     1. Lack of good reporting tools within the company
#     2. Inadequate data to work on
#     3. The quality of the data could be poor
#     4. Mechanical challenges could also be encountered during tracking and reporting stage.

# In[ ]:




