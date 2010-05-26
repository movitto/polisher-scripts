# puppet polisher registration

project :name => 'puppet' do |puppet|
  puppet.add_archive :name => 'puppet',        :uri => 'http://reductivelabs.com/downloads/puppet/puppet-%{version}.tar.gz', :primary_source => true
  puppet.add_file    :name => 'puppet.sign',   :uri => 'http://reductivelabs.com/downloads/puppet/puppet-%{version}.tar.gz.sign'
  puppet.add_patch   :name => 'correct-rundir-permissions', :uri => "#{@fedora_cvs}/puppet-0.25.1-0002-Correct-rundir-permissions.patch?view=co"

  puppet.on_version "*",             "download sources"
  puppet.on_version "*",             "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  puppet.on_version "*",             "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
  puppet.on_version "=",   "0.25.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable"
  puppet.on_version ">=",  "0.25.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance"
  puppet.on_version ">=",  "0.25.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"
end
