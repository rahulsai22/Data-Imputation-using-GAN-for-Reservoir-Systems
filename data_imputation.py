

from torch import nn
import math
import matplotlib.pyplot as plt
torch.manual_seed(111)
import pandas as pd

df1 = pd.read_csv("Ravi(1).csv")
#df1['Outflow (MCM)']=df1['Outflow (MCM)'].replace(0,df1['Outflow (MCM)'].mean())

"""
Input : Inflow
Generating output for Gross storage at the end
"""

import numpy as np
train_data_length = 324
train_data = torch.zeros((train_data_length, 6))

#p1 =  np.genfromtxt('Ravi_gan.csv',delimiter=',',usecols=np.arange(0,8))
# q1 = initial level , inflow , evap , storage at start and outflow ;
# And r1 are all the input values and r1 = storage ; is the required output for generating new data...

p1 = df1.iloc[:, 0:9]
q1 = df1.iloc[1:327,2:7]
r1 = p1.iloc[1:327,8]

#inflow of 1025 rows
a =  np.genfromtxt('c1.csv')
a1 = a[1:325]

#evaporation of 1025 rows
b =  np.genfromtxt('c2.csv')
b1 = b[1:325]

#storage at end of 1025 rows
c = np.genfromtxt('c3_2.csv')
c1 = c[1:325]

#outflow/Irrigation Release/Domestic Release of 1025 rows
d = np.genfromtxt('Ravi_outflow.csv',delimiter=',',usecols=(0))
d1 = d[1:325]
#d1 = df1.iloc[0:325, 8]
#print(d1)

#Initial_level
e = np.genfromtxt('Initial_level.csv',delimiter=',',usecols=(0))
e1 = e[1:325]

#Gross storage at start"
f = np.genfromtxt('Gross storage at start.csv',delimiter=',',usecols=(0))
f1 = f[1:325]

train_data[:, 0] = torch.Tensor(a1)
train_data[:, 1] = torch.Tensor(b1)
train_data[:, 2] = torch.Tensor(c1)
train_data[:, 3] = torch.Tensor(d1)
train_data[:, 4] = torch.Tensor(e1)
train_data[:, 5] = torch.Tensor(f1)

#c1 = c1.reshape(1024,1)
#b1 = b1.reshape(1024,1)
#a1 = a1.reshape(1024,1)
#x = np.concatenate((a1, b1), axis=1)

#x1 = a[151:151+200]

#x1 = x1.reshape(100,2)
#t = np.concatenate((a1,c1, b1), axis=1)

test1 = np.concatenate((a1,b1,c1,d1,e1,f1))

train_labels = torch.zeros(train_data_length)
train_set = [
    (train_data[i], train_labels[i]) for i in range(train_data_length)]

print(train_data.shape,train_labels.shape)

#1.inflow  2.Evap 3.Storage at end 4.Outflow / Irrigation Release 5.Initial level 6.Storage at start

"""
Input : Inflow
Generating output for Gross storage at the end
"""

"""
import pandas as pd
import numpy as np
train_data_length = 324
train_data = torch.zeros((train_data_length, 6))


import pandas as pd
import matplotlib.pyplot as mp

# take data
data = pd.read_csv("Ravi_gan.csv")

df = pd.DataFrame(data,
                  columns=["Gross Storage at End (4+5)-(6+13+14) (MCM)",
                            "Inflow (MCM),Evaporation (MCM)","Outflow (MCM)"])

# plot the dataframe
df.plot(x="Gross Storage at End (4+5)-(6+13+14) (MCM)", y=["Inflow (MCM),Evaporation (MCM)","Outflow (MCM)"], kind="bar", figsize=(90, 80))

# print bar graph
mp.show()

p1 =  np.genfromtxt('Ravi_gan.csv',delimiter=',',usecols=np.arange(0,8))

# q1 = initial level , inflow , evap , storage at start and outflow ;
# And r1 are all the input values and r1 = storage ; is the required output for generating new data...

q1 = p1[1:327,[2,3,4,5,6]]
r1 = p1[1:327,7]

#inflow of 1025 rows
a =  np.genfromtxt('c1.csv')
a1 = a[1:325]


#evaporation of 1025 rows

b =  np.genfromtxt('c2.csv')
b1 = b[1:325]


#storage at end of 1025 rows
c = np.genfromtxt('c3_2.csv')
c1 = c[1:325]



#outflow of 1025 rows
d = np.genfromtxt('c4.csv',delimiter=',',usecols=(0))
d1 = d[1:325]

train_data[:, 0] = torch.Tensor(a1)
train_data[:, 1] = torch.Tensor(b1)
train_data[:, 2] = torch.Tensor(c1)
train_data[:, 3] = torch.Tensor(d1)

#c1 = c1.reshape(1024,1)
#b1 = b1.reshape(1024,1)
#a1 = a1.reshape(1024,1)
#x = np.concatenate((a1, b1), axis=1)

#x1 = a[151:151+200]

#x1 = x1.reshape(100,2)
#t = np.concatenate((a1,c1, b1), axis=1)

train_labels = torch.zeros(train_data_length)
train_set = [
    (train_data[i], train_labels[i]) for i in range(train_data_length)]

print(q1.shape,r1.shape)
print(train_data.shape,train_labels.shape)
"""

plt.plot(train_data[:, 0], train_data[:, 2], ".")

batch_size = 18
train_loader = torch.utils.data.DataLoader(
    train_set, batch_size=batch_size, shuffle=True
)

"""
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(6, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        output = self.model(x)
        return output
"""
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(6, 1024),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        output = self.model(x)
        return output

discriminator = Discriminator()

class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(6, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 6),
        )

    def forward(self, x):
        output = self.model(x)
        return output

generator = Generator()

lr = 0.01
num_epochs = 500
#loss_function = nn.BCELoss()

loss_function = nn.MSELoss()

optimizer_discriminator = torch.optim.Adam(discriminator.parameters(), lr=lr)
optimizer_generator = torch.optim.SGD(generator.parameters(), lr=lr)

for epoch in range(num_epochs):
    for n, (real_samples, _) in enumerate(train_loader):
        # Data for training the discriminator
        real_samples_labels = torch.ones((batch_size, 1))

        latent_space_samples = torch.randn((batch_size, 6))
        generated_samples = generator(latent_space_samples)
        generated_samples_labels = torch.zeros((batch_size, 1))

        all_samples = torch.cat((real_samples, generated_samples))
        print(real_samples_labels.shape, generated_samples_labels.shape)
        all_samples_labels = torch.cat(
            (real_samples_labels, generated_samples_labels)
        )

        # Training the discriminator
        discriminator.zero_grad()
        output_discriminator = discriminator(all_samples)
        loss_discriminator = loss_function(
            output_discriminator, all_samples_labels)
        loss_discriminator.backward()
        optimizer_discriminator.step()

        # Data for training the generator
        latent_space_samples = torch.randn((batch_size, 6))

        # Training the generator
        generator.zero_grad()
        generated_samples = generator(latent_space_samples)
        output_discriminator_generated = discriminator(generated_samples)
        loss_generator = loss_function(
            output_discriminator_generated, real_samples_labels
        )
        loss_generator.backward()
        optimizer_generator.step()

        # Show loss
        if epoch % 10 == 0 and n == batch_size - 1:
            print(f"Epoch: {epoch} Loss D.: {loss_discriminator}")
            print(f"Epoch: {epoch} Loss G.: {loss_generator}")

"""

latent_space_samples = torch.Tensor(train_data)
latent_space_samples1 = torch.randn(100,6)

generated_samples = generator(latent_space_samples1)
generated_samples_test1 = generator(latent_space_samples)
"""

latent_space_samples = torch.Tensor(train_data)
latent_space_samples1 = torch.randn(100,6)


generated_samples = generator(latent_space_samples1)
generated_samples_test1 = generator(latent_space_samples)
print(train_data) #inflow, evap, GS at end , outflow, initial level, GS at start

generated_samples_test1
#inflow, evap, GS at end , outflow/Irrigation_release, initial level, GS at start

generated_samples


#For simple tables, you can also export by converting the tensor to a Numpy array and then to a Pandas dataframe.


t = torch.tensor(generated_samples_test1) #dummy data

t_np = t.numpy() #convert to Numpy array
df = pd.DataFrame(t_np) #convert to a dataframe
df.to_csv("GAN_Ravi_Outflow.csv",index=True) #save to file

#Then, to reload:
df = pd.read_csv("GAN_Ravi_Outflow.csv")
df

df2 = pd.read_csv('GAN_Ravi_Outflow.csv')
df3 = df2['3']
df1['GAN_Ravi_Outflow'] = df3

df1
p = df1.to_csv('GAN_Ravi_Outflow.csv')

p1 = pd.read_csv('/content/ravishankarmulti.csv')

px = pd.read_csv('GAN_Ravi_Outflow.csv')

p4 = px
#print(px)

p4['Outflow_GAN'] = px['3']
#p4['IR_GAN'] = px['IR_GAN']
#p4['domestic_release_GAN'] = px['domestic_release_GAN']
#p4['domestic_release_GAN'] = px['industrial_release_GAN']

p4=p4.to_csv("Ravi_multi_updated.csv")

#mean_value=p1['Domestic Release(MCM)'].mean()
#p1['Domestic Release(MCM)'].fillna(value=mean_value, inplace=True)
#p1['Domestic Release(MCM)'].fillna(int(p1['Domestic Release(MCM)'].mean()), inplace=True)

X = p1.iloc[:,8:9].values

# To calculate mean use imputer class
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X)

X = imputer.transform(X)
print(X)

p1["B"] = X
p2 = p1["B"]
p2 = p2.to_csv("industrial_release_with_mean.csv")


p3 = p1.iloc[:,10:11]
p3 = p3.to_csv("Industrial_demand.csv")

"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization library
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import time
from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))
#import warnings library
import warnings
# ignore all warnings
warnings.filterwarnings('ignore')


data = pd.read_csv('Ravi(1).csv')


data.head()


col = data.columns       # .columns gives columns names in data
print(col)

# y includes our labels and x includes our features
y = data.Output                         # M or B
list = ['S. No.','Year/ Month']
x = data.drop(list,axis = 1 )
x.head()


ax = sns.countplot(y,label="Count")       # M = 212, B = 357
"""
"""
B, M = y.value_counts()
print('Number of Benign: ',B)
print('Number of Malignant : ',M)
"""
"""
x.describe()

# first ten features
data_dia = y
data = x
data_n_2 = (data - data.mean()) / (data.std())              # standardization
data = pd.concat([y,data_n_2.iloc[:,0:10]],axis=1)

print(data.shape)
data.values.flatten()
print(data.shape)

#data.reshape(2268,1)
data = data.to_numpy()
data.flatten()
data = pd.melt(data,id_vars="Output",var_name="features",value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="Output", data=data,split=True, inner="quart")
plt.xticks(rotation=90)



# first ten features
data_dia = y
data = x
data_n_2 = (data - data.mean()) / (data.std())              # standardization
data = pd.concat([y,data_n_2.iloc[:,0:10]],axis=1)
data = pd.melt(data,id_vars="diagnosis",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="diagnosis", data=data,split=True, inner="quart")
plt.xticks(rotation=90)
"""

plt.plot(train_data[ :,0],train_data[:, 3], ".")

generated_samples_t1 = generated_samples.detach()
plt.plot(train_data[1:101, 0],generated_samples_t1[:, 3], ".")

plt.plot(train_data[1:101, 0],train_data[1:101, 3], ".")

plt.plot(train_data[:,0],train_data[:,1])

generated_samples = generated_samples.detach()

plt.plot(generated_samples[:,0],generated_samples[:,1])

plt.plot(train_data[:,0],train_data[:,2])

plt.plot(train_data[:,0],train_data[:,3])

plt.plot(train_data[:,0],train_data[:,4])

plt.plot(train_data[:,0],train_data[:,5])

plt.plot

latent_space_samples1

print(latent_space_samples.shape)
print(generated_samples_test1 .shape)
print(train_data.shape)

"""generated_samples_test1"""

data1 = pd.read_csv('testfile.csv')



data1.rename(columns = {'3':'Irrigation release'}, inplace = True)
col1 = data1.columns       # .columns gives columns names in data

print(col1)
y1 = data1['Irrigation release']                         # M or B
list1 = ['Irrigation release']
x1 = data1.drop(list1,axis = 1 )
x1.head()
#y1 = data1.5
# M or B
#list1 = ['5']
#x1 = data1.drop(list,axis = 1 )
#x1.head()


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization library
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import time
from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))
#import warnings library
import warnings
# ignore all warnings
warnings.filterwarnings('ignore')
# Any results you write to the current directory are saved as output.


data_dia1 = y1
data1 = x1
data_n_21 = (data1 - data1.mean()) / (data1.std())              # standardization
data1 = pd.concat([y1,data_n_21.iloc[:,0:10]],axis=1)
data1 = pd.melt(data1,id_vars="Irrigation release",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x1="features", y1="value", data=data1,split=True, inner="quart")
plt.xticks(rotation=90)

data2 = pd.read_csv('testfile.csv')



data2.rename(columns = {'3':'Irrigation release'}, inplace = True)
col2 = data2.columns       # .columns gives columns names in data

print(col2)
y2 = data2['Irrigation release']                         # M or B
list2 = ['Irrigation release']
x2 = data2.drop(list2,axis = 1 )
x2.head()



data_dia2 = y2
data2 = x2
data_n_22= (data2 - data2.mean()) / (data2.std())              # standardization
data2 = pd.concat([y2,data_n_22.iloc[:,0:10]],axis=1)
data2 = pd.melt(data2,id_vars="Irrigation release",
                    var_name="features",
                    value_name='value')
plt.figure(figsize=(10,10))
sns.violinplot(x = "features", y = "value", data=data2,split=True, inner="quart")
plt.xticks(rotation=90)

train_data

generated_samples_test1

generated_samples_t2 = generated_samples_test1.detach()
generated_samples_t2.numpy()

train_data.numpy()

#Error calculation

mse = ((generated_samples_t2.numpy() - train_data.numpy())**2).mean(axis=0)
mse

#Output : Average of all the six column values after applying MSE.

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(generated_samples_t2.numpy(), train_data.numpy())
mse



generated_samples = generated_samples.detach()

plt.plot(generated_samples[:, 0],generated_samples[:, 1], generated_samples[:, 2], ".")
print(generated_samples.shape)

#Output of new generated samples

plt.plot(train_data[:, 0], train_data[:, 3], ".")

"""generated_samples = generated_samples.detach()

plt.plot(generated_samples[:, 0],generated_samples[:, 2], ".")
"""

plt.plot(train_data[:, 0],train_data[:, 1] ,train_data[:, 2], ".")

#Original Data output

generated_samples_test1 = generated_samples_test1.detach()

plt.plot(train_data[:, 0],generated_samples_test1[:, 2], ".")

plt.plot(train_data[:, 0], train_data[:, 2], ".")

generated_samples = generated_samples.detach()

plt.plot(train_data[1:101, 0],generated_samples[:, 2], ".")

"""
tens = torch.sub(latent_space_samples, generated_samples)

# display result after perform element wise
# subtraction
print(" After Element-wise subtraction: ", tens)
plt.plot(tens.to('cpu').numpy())
"""

latent_space_samples

print(generated_samples_t1)
print(latent_space_samples)

