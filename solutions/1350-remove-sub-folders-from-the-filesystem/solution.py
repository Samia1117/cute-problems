class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # create a dictionary 'roots', of the form root_folder:[subfolder1, subfolder2]
        # return the number of keys in the dictionary
        
        folder_set = set(folder)
        print(f'folder set = {folder_set}')
        results = []

        for f in folder:
            # print(f"Results = {results}")
            is_subfolder = False
            prefix = f 

            while prefix != '':
                parent_index = prefix.rfind('/')
                if parent_index == -1:
                    break
                prefix = prefix[0:parent_index]
                # print("folder prefix is: ", prefix)

                if prefix in folder_set:
                    # print(f'Prefix = {prefix} is a subfolder')
                    is_subfolder = True
                    break
                    # print("Prefix is not a subfolder")
            if not is_subfolder:
                # print(f'Prefix = {f} is a NOT a subfolder')
                results.append(f)

        return results

        
