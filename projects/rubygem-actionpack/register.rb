# rubygem-actionpack polisher registration

# should be named rubygem-actionpack but isn't currently in Fedora

project :name => 'rubygem-actionpack' do |actionpack|
  actionpack.add_gem :name => 'actionpack', :uri => 'http://rubygems.org/downloads/actionpack-%{version}.gem', :primary_source => true

  actionpack.add_patch   :name => 'rubygem-actionpack-enable-test.patch', :uri => "#{@morsiorg_polisher_sources}/rubygem-actionpack-2.3.8-enable-test.patch"
  #actionpack.add_patch   :name => 'rubygem-actionpack-rack-compat.patch', :uri => "#{@morsiorg_polisher_sources}/rubygem-actionpack-2.3.8-rack-compat.patch"

  actionpack.on_version "*",           "download sources"

  actionpack.on_version "=",  "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  actionpack.on_version "=",  "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  actionpack.on_version ">=", "2.3.8", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  actionpack.on_version ">=", "2.3.8", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  # uncomment when Ruby 1.9 supports rails 3
  #actionpack.on_version "=",  "3.0.0", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  #actionpack.on_version ">=", "3.0.0", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  actionpack.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
