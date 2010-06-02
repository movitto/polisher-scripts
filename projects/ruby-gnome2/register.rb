# ruby-gnome2 polisher registration

project :name => 'ruby-gnome2' do |rg2|
  rg2.add_archive :name => 'ruby-gnome2', :uri => 'http://downloads.sourceforge.net/ruby-gnome2/ruby-gnome2-all-%{version}.tar.gz', :primary_source => true
  rg2.add_patch   :name => 'ruby-gnome2-0.17.0-rc1-script', :uri => "#{@fedora_cvs}/ruby-gnome2-0.17.0-rc1-script.patch?view=co"

  rg2.version "*", :depends_on => project(:name => 'ruby')
  rg2.version "*", :depends_on => project(:name => 'cairo')

  rg2.on_version "*",           "download sources"

  rg2.on_version "=",  "0.19.4", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @stable_mock_env
  rg2.on_version "=",  "0.19.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/stable", :delete_rpms => true

  # TODO uncomment when ruby 1.8.7 is setup in maintenance repo
  #rg2.on_version ">=", "0.19.4", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @maintenance_mock_env
  #rg2.on_version ">=", "0.19.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/maintenance", :delete_rpms => true

  rg2.on_version ">=", "0.19.4", "create rpm package", :spec => "#{@project_dir}/template.spec", :mock => @devel_mock_env
  rg2.on_version ">=", "0.19.4", "update yum repo",    :repo => "#{@artifacts_dir}/repos/devel"

  rg2.on_version "*",           "update yum repo",     :repo =>"#{@artifacts_dir}/repos/rawhide"
end
