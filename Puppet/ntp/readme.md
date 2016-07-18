# Configuring NTP on nodes

1. Install ntp module from Puppet Forge

```   puppet module install puppetlabs-ntp```

2. Classification using site.pp manifest 

```emacs /etc/puppetlabs/code/environments/production/manifests/site.pp```

   Edit the site.pp manifest to specify the node. We also use ntp class declaration to specify the array of ntp server we use to sync time.

   Please see the site.pp manifest file in the directory to check out the implementation.

   NOTE : Classification of node can be alternatively performed using Puppet Console.

3. Validate site.pp manifest for errors

```puppet parser validate ```

4. Run Puppet agent

```puppet agent -t```

5. Check if the ntp is installed and configured correctly

```puppet resource package ntp```
```puppet resource service ntpd```

