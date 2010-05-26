# rubygems polisher registration

project :name => 'rubygems' do |rubygems|
  rubygems.add_archive :name => 'rubygems',      :uri => 'http://rubyforge.org/frs/download.php/%{repoid}/rubygems-%{version}.tgz'
  rubygems.add_patch   :name => 'noarch-gemdir', :uri => "#{@fedora_cvs}/rubygems-1.3.5-noarch-gemdir.patch?view=co"

  rubygems.on_version "*",           "download sources"
  rubygems.on_version "*",           "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @system_mock_env
  rubygems.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
  rubygems.on_version "=",  "1.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable"
  rubygems.on_version ">",  "1.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance"
  rubygems.on_version ">",  "1.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"
end
