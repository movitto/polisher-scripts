# rubygems polisher registration

project :name => 'rubygems' do |rubygems|
  rubygems.add_archive :name => 'rubygems',      :uri => 'http://rubyforge.org/frs/download.php/%{repoid}/rubygems-%{version}.tgz'
  rubygems.add_patch   :name => 'noarch-gemdir', :uri => "#{@fedora_cvs}/rubygems-1.3.7-noarch-gemdir.patch?view=co"

  rubygems.version "*", :depends_on => project(:name => 'ruby')

  rubygems.on_version "*",           "download sources"

  # starting in ruby 1.9 rubygems is included as part of
  # the official ruby project proper. still provide package for
  # the devel repo, but it will be empty / pull in ruby

  rubygems.on_version "=",  "1.3.5", "create rpm package", :spec => "#{@project_dir}/template-1.8.spec", :mock => @stable_mock_env
  rubygems.on_version "=",  "1.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #rubygems.on_version ">",  "1.3.5", "create rpm package", :spec => "#{@project_dir}/template-1.8.spec", :mock => @maintenance_mock_env
  #rubygems.on_version ">",  "1.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  rubygems.on_version ">",  "1.3.5", "create rpm package", :spec => "#{@project_dir}/template-1.9.spec", :mock => @devel_mock_env
  rubygems.on_version ">",  "1.3.5", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  rubygems.on_version "*",           "update yum repo",    :repo => "#{@artifacts_dir}/repos/rawhide"
end
