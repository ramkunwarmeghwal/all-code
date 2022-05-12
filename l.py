import re
from unicodedata import name
from webbrowser import get
from flask import Flask, render_template, request
import boto3
import pprint
import pandas as pd

boto3.setup_default_session(profile_name='staging')


client = boto3.client('autoscaling',region_name='ap-south-1')

response = client.describe_auto_scaling_groups()

app = Flask(__name__)





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


df.columns =['ASG_TAG', 'Availibility_zone', 'MaxSize', 'MinSize','desiredCapicity','HealthCheckGracePeriod','Instances(InstanceId and Type)', 'Tags(Key and Value)']



@app.route('/second',methods=("POST", "GET"))
def second():
    AutoScalingGroupName = request.form['stars']
    #username = "abcd"
    MinSize = request.form['minsize']
    MaxSize = request.form['maxsize']

    MinSize = int(MinSize)
    MaxSize = int(MaxSize)
    
    client = boto3.client('autoscaling',region_name='ap-south-1')
    response = client.update_auto_scaling_group(AutoScalingGroupName=AutoScalingGroupName,MaxSize=MaxSize,MinSize=MinSize)
   
    #return "username is "+ " " + username + "minsize is  "+" "+ str(minsize) + " "+"maxsize is  " + str(maxsize);
    return "Value update successfully" 

@app.route('/attach',methods=('POST','GET'))
def attach():
    AutoScalingGroupName = request.form['stars']
    InstanceId = request.form['instancid']

    response = client.attach_instances(
    InstanceIds=[
        InstanceId
    ],
    AutoScalingGroupName=AutoScalingGroupName)
    return "Instances is Attached"
   

@app.route('/')
def my_form():
    return render_template('l.html')
   

@app.route('/abc',methods=['post','get'])
def abc():
     return(render_template('d.html',review=list(zip(ASG_tag,Availibility_zone,MaxSize,MinSize,desiredCapicity,l,lm))))




if __name__=='__main__':
    app.run(debug=True)    
