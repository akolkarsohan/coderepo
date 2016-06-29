# See http://docs.chef.io/config_rb_knife.html for more information on knife configuration options

current_dir = File.dirname(__FILE__)
log_level                :info
log_location             STDOUT
node_name                "akolkarsohan"
client_key               "#{current_dir}/akolkarsohan.pem"
validation_client_name   "sohochef-validator"
validation_key           "~/Chef/sohochef-validator.pem"
chef_server_url          "https://api.chef.io/organizations/sohochef"
cookbook_path            ["#{current_dir}/../cookbooks","~/Documents/Chef/learn-chef/cookbooks"]
