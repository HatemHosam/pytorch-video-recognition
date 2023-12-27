class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = '/data/i5O/UCF-101'

            # Save preprocess data into output_dir
            output_dir = '/data/i5O/post_process/UCF-101'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        elif database == 'kinetics400':
            # folder that contains class labels
            root_dir = '/data/i5O/k400/videos'

            output_dir = '/data/i5O/post_process/kinetics400'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return 'Models/c3d-pretrained.pth'
