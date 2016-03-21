import harddrive

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
            self.disk.add(filename, content, '/')
        elif command == 'dir create':
            dir_name = raw_input('Directory name # :')
            self.disk.create_dir(dir_name)
        elif command == '-a dir':
            for i in self.disk.file_space:
                print i
        elif command == 'cd':
            dir_name = raw_input('What directory do you want to enter? # :')
            self.disk.go_inside_directory(dir_name)
            self.disk.open_directory()
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
            print file_name
            self.disk.delete_file(file_name)
        elif command == 'file open':
            file_name = raw_input("filename # :")
            file_name += '/'
            print self.disk.open_file(file_name)
        elif command == 'file rename':
            file_name = raw_input('Filename # :')
            new_file_name = raw_input('new filename # :')
            self.disk.rename_file(file_name, new_file_name)

    def dir(self, pos):
        pass


cmd = Commands()
while True :
    cmd.makeCommand()