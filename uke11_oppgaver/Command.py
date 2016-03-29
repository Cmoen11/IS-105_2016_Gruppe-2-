import harddrive
import os
class Commands:
    def __init__(self):
        self.disk = harddrive.SSD()

    def makeCommand(self):
        command = raw_input('# :')
        if command == 'dir':
            self.disk.open_directory()

        elif command == 'file create':
            filename = raw_input('filename # :')
            content = raw_input('content # :')
            if not self.disk.filename_exist(filename):
                self.disk.add(filename, content, '/')
            else:
                print 'Operation cancelled: A file with that name already exist.'

        elif command == 'dir create':
            dir_name = raw_input('Directory name # :')
            if not self.disk.dirname_exist(dir_name+'/'):
                self.disk.create_dir(dir_name)
            else :
                print 'Operation cancelled: A directory with that name already exist.'

        elif command == '-a dir':
            for i in self.disk.file_space:
                print i

        elif command == 'cd':
            dir_name = raw_input('What directory do you want to enter? # :')
            dir_name += '/'
            #print dir_name
            answer = self.disk.go_inside_directory(dir_name)
            if answer == False :
                print 'Operation cancelled: No directory is called by that name.'

        elif command == 'cd ..':
            self.disk.go_outside_directory()
            self.disk.open_directory()

        elif command == 'dir delete':
            dir_name = raw_input("What directory do you want to delete? # :")
            dir_name += '/'

            self.disk.delete_dir(dir_name)
        elif command == 'file delete':
            file_name = raw_input("what file do you want to delete? # :")
            file_name += '/'
            #print file_name
            self.disk.delete_file(file_name)

        elif command == 'file open':
            file_name = raw_input("filename # :")
            #file_name += '/'
            print self.disk.open_file(file_name)

        elif command == 'file rename':
            file_name = raw_input('Filename # :')
            new_file_name = raw_input('new filename # :')
            answer = self.disk.rename_file(file_name, new_file_name)
            if answer is False :
                print 'Operation cancelled: A file with that name already exist.'

        elif command == 'dir rename':
            dir_name = raw_input('Directory name # :')
            new_dir_name = raw_input('new Directory name # :')
            dir_name += '/'
            new_dir_name += '/'
            answer = self.disk.rename_dir(dir_name, new_dir_name)
            if answer is False:
                print 'Operation cancelled: A directory with that name already exist.'

        elif command == 'clear':
            os.system('cls' if os.name=='nt' else 'clear')

        elif command == 'stat':
            self.disk.stats()

        elif command == 'file copy':
            filename = raw_input('Filename #:')
            copyname = raw_input('Name of the copy #:')

            if self.disk.file_copy(filename,copyname) == False:
                print 'There are no files with that filename or copyname is already beeing used.'

    def dir(self, pos):
        pass


cmd = Commands()
while True :
    cmd.makeCommand()