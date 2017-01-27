#!/bin/bash

#################################################################
# USAGE : stop-aws-instances.sh profile region                  # 
# Example : stop-aws-instances.sh SohanAkolkar ap-south-1       #
#################################################################

get_profile=$1
get_region=$2

aws_list_instances="aws ec2 describe-instances --query  "Reservations[].Instances[].[Placement.AvailabilityZone,State.Name,InstanceId,NetworkInterfaces[0].Association.PublicIp,KeyName,Tags[0].Value]" --output table"

get_running_instances=$($aws_list_instances --region $get_region --profile $get_profile | grep running | awk '{print $5}')

echo "Stopping Running EC2 instances"

aws ec2 stop-instances --instance-id $get_running_instances --profile $get_profile --region $get_region 

echo "Stopped all running EC2 instances"
