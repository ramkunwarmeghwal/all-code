from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import boto3
import pprint

boto3.setup_default_session(profile_name='staging')
client = boto3.client('autoscaling',region_name='ap-south-1')


app = Flask(__name__)

response = client.describe_auto_scaling_groups()
#pprint.pprint(response)

ASG_tag = []
Availibility_zone = []
desiredCapicity = []
HealthCheckGracePeriod = []
LoadBalancerNames = []
MaxSize = []
MinSize = []
LaunchTemplateId = []
Tags = []
Value = []
Instances = []
VPCZoneIdentifier = []
#MixedInstancesPolicy = []
l1 = []
instance_type = []
ls = [] 
all_asg = response['AutoScalingGroups']

c = []
d = []

e = []
f = []


for i in all_asg:
    #print(i['AutoScalingGroupName'])
    ASG_tag.append(i['AutoScalingGroupName'])
    Availibility_zone.append(i['AvailabilityZones'])
    desiredCapicity.append(i['DesiredCapacity'])
    HealthCheckGracePeriod.append(i['HealthCheckGracePeriod'])
    LoadBalancerNames.append(i['LoadBalancerNames'])
    MaxSize.append(i['MaxSize'])
    MinSize.append(i['MinSize'])
    Tags.append(i['Tags'])
    
    l3 = []
    l4 = []
    for j in Tags:
        if j==[]:
            l3.append("-")
            l4.append("-")
        else:   
            for dic in j:
                    name = dic.get('Key')
                    l3.append(name)
                    value = dic.get('Value')
                    l4.append(value)
            e.append(l3)
            f.append(l4)
    Tags = []                
    #pprint.pprint(list(zip(l3,l4)))    
    
    
    
    
    
    
    Instances.append(i['Instances'])
    
    
    l1=[]
    l2=[]
    
    for k in Instances:
        if k==[]:
            l1.append("-")
            l2.append("-")
            c.append(l1)
            d.append(l2)
        else:   
            for dic in k:
                    name = dic.get('InstanceType')
                    l1.append(name)
                    Instanceid = dic.get('InstanceId')
                    l2.append(Instanceid)
            c.append(l1)
            d.append(l2)
                    
    Instances = []    

Instances = list(zip(d,c))
#print(Instances)
lm = []
tags = list(zip(e,f))
for i in tags:
        #pprint.pprint(dict(zip(i[0],i[1])))
        lm.append(dict(zip(i[0],i[1])))


l = []
for i in Instances:
    l.append((dict(zip(i[0],i[1]))))

# tags = list(zip(e,f))
# l6 = []
# for j in tags:
#     l6.append((dict(zip(i[0],i[1]))))


df = pd.DataFrame(
    {'ASG_tag': ASG_tag,
     'Availibility_zone': Availibility_zone,
     'MaxSize': MaxSize,
     'MinSize': MinSize,
     'desiredCapicity': desiredCapicity,
     'HealthCheckGracePeriod': HealthCheckGracePeriod,
     'Instances(InstanceId and Type)':l,
     'Tags(Key and Value)': lm
     #'Instances': list(zip(d,c)),

    #  'Tags(Key and Value)': l6
    })


df.columns =['ASG_TAG', 'Availibility_zone', 'MaxSize', 'MinSize','desiredCapicity','HealthCheckGracePeriod','Instances', 'Tags(Key and Value)']






@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

# @app.route('/name',methods=("POST", "GET"))
# def asg():
#     return "I already Clicked !!"
    #p=(ASG_tag.index(input("Enter name")))
    #return(df.iloc[[p]])
#     return render_template('friends.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
      app.run()