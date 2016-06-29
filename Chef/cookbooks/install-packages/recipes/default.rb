#
# Cookbook Name:: install-packages
# Recipe:: default
#
# Copyright (c) 2016 The Authors, All Rights Reserved.
# Author : Sohan Akolkar
# History : May 2016 - initial creation of the recipe

# Install packages on nodes
package ['emacs','wget','firewalld','iptables-services','nmap','httpd','pinfo'] do
  action :install
end

service 'httpd' do
  action :restart
end
