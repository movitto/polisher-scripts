# rubygem-mongrel polisher registration

project :name => 'rubygem-mongrel' do |mongrel|
  mongrel.add_gem :name => 'mongrel',   :uri => 'http://rubygems.org/gems/mongrel-%{version}.gem', :primary_source => true
  mongrel.add_gem :name => 'multipart', :uri => 'http://gems.rubyforge.org/gems/cgi_multipart_eof_fix-2.5.0.gem'

  mongrel.on_version "*", "create rpm package", "#{@project_dir}/template.spec"
  mongrel.on_version "*",           "update yum repo", "#{@artifacts_dir}/repos/rawhide"
  mongrel.on_version "=",  "1.1.5", "update yum repo", "#{@artifacts_dir}/repos/stable"
  mongrel.on_version ">=", "1.2.0", "update yum repo", "#{@artifacts_dir}/repos/maintenance"
  mongrel.on_version ">=", "1.2.0", "update yum repo", "#{@artifacts_dir}/repos/devel"
end
