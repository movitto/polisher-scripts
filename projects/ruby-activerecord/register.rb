# rubygem-activerecord polisher registration

# should be named rubygem-activerecord but isn't currently in Fedora

project :name => 'ruby-activerecord' do |activerecord|
  activerecord.add_gem :name => 'activerecord', :uri => 'http://rubygems.org/downloads/activerecord-%{version}.gem', :primary_source => true

  activerecord.on_version "*",           "create rpm package", "#{@project_dir}/template.spec"
  activerecord.on_version "*",           "update yum repo",    "#{@artifacts_dir}/repos/rawhide"
  activerecord.on_version "=",  "2.0.1", "update yum repo",    "#{@artifacts_dir}/repos/stable"
  activerecord.on_version "=",  "2.3.5", "update yum repo",    "#{@artifacts_dir}/repos/maintenance"
  activerecord.on_version ">=", "3.0.0", "update yum repo",    "#{@artifacts_dir}/repos/devel"
end
