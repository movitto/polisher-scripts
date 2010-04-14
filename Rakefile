# polisher project rakefile

# FIXME
require '../polisher/lib/dsl.rb'

# FIXME
@artifacts_dir = '../polisher/artifacts'

# TODO make this configurable
polisher "http://localhost:3000"

@morsiorg_polisher_sources = "http://projects.morsi.org/polisher/sources"

desc "register all projects"
task :register do
  scripts = Dir['projects/*/register.rb']
  scripts = ["projects/#{ENV['project']}/register.rb"] unless ENV['project'].nil?

  scripts.each { |rs| 
    @project_dir  = File.expand_path(File.dirname(rs))
    @project_name = File.dirname(rs).split('/').last
    @fedora_cvs   = "http://cvs.fedoraproject.org/viewvc/rpms/#{@project_name}/F-13"
    load rs 
  }
end

desc "remove all projects"
task :remove do
  scripts = Dir['projects/*/remove.rb']
  scripts = ["projects/#{ENV['project']}/remove.rb"] unless ENV['project'].nil?

  scripts.each { |rs| 
    load rs 
  }
end

desc "trigger a release on all projects"
task :release do
  scripts = Dir['projects/*/release.rb']
  scripts = ["projects/#{ENV['project']}/release.rb"] unless ENV['project'].nil?

  scripts.each { |rs| 
    @projects_dir =  File.expand_path(File.dirname(rs))
    load rs 
  }
end
