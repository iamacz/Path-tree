import os  
  
path = ""  
  
def list_files(startpath):  
    with open("{}\\Index.md".format(path), "w") as f:  
        for root, dirs, files in os.walk(startpath):  
            # Remove dirs[:] to prevent os.walk from visiting excluded directories  
            dirs[:] = [d for d in dirs if d not in ['.git',".trash"]]  
            level = root.replace(startpath, '').count(os.sep)  
            indent = '#' * (level + 1)  
            f.write('\n{} {}\n'.format(indent, os.path.basename(root)))  
            for filename in files:  
                # remove some files  
                if filename not in ['.gitignore']:  
                    # Check if the file is a markdown file  
                    if filename.endswith('.md') or filename.endswith('.canvas'):  
                        # Write the file name without extension and within brackets  
                        f.write('- [[{}]]{}\n'.format(os.path.splitext(filename)[0],
						      os.path.splitext(filename)[1]))
                    else:  
                        f.write('- {}\n'.format(filename))  
  
                    # Now we call the function and pass in the directory we want to start in.  
  
  
# To get all files and folders under the current directory, we can use '.'  
list_files(path)

print("The index has been updated!")
