class create_data:
    
    def files_path(path):
        files_images=os.listdir(path)
        return np.asarray(files)
    def main(path_to_data, path_to_test_data, train_ratio):
   
    _, dirs, _ = next(os.walk(path_to_data))


    data_counter_per_class = np.zeros((len(dirs)))
    for i in range(len(dirs)):
        path = os.path.join(path_to_data, dirs[i])
        files = get_files_from_folder(path)
        data_counter_per_class[i] = len(files)
    test_counter = np.round(data_counter_per_class * (1 - train_ratio))

    
    for i in range(len(dirs)):
        path_to_original = os.path.join(path_to_data, dirs[i])
        path_to_save = os.path.join(path_to_test_data, dirs[i])

       
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)
        files = get_files_from_folder(path_to_original)
     
        for j in range(int(test_counter[i])):
            dst = os.path.join(path_to_save, files[j])
            src = os.path.join(path_to_original, files[j])
            shutil.move(src, dst)


    def parse_args():
      parser = argparse.ArgumentParser(description="Dataset divider")
      parser.add_argument("--data_path", required=True,
        help="Path to data")
      parser.add_argument("--test_data_path_to_save", required=True,
        help="Path to test data where to save")
      parser.add_argument("--train_ratio", required=True,
        help="Train ratio - 0.7 means splitting data in 70 % train and 30 % test")
      return parser.parse_args()
