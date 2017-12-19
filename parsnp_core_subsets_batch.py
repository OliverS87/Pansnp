# Run parsnp on a collection of sequences (+ a reference)
# Generate sets with sequentially increasing size:
# Start with 2, add more to go to 5, 10, 20, 50, 100, 200, 300, 400

import sys
import os
from SimpleParSNP import SimpleParSNP


if __name__ == '__main__':
    if len(sys.argv[1:]) != 8:
        print("Usage: python3 {0} reference sample_dir distance_value cpu_count out_folder substract sets prefix".format(
            sys.argv[0]))
        exit(3)
    ref_path = sys.argv[1]
    dist_val = int(sys.argv[3])
    cpu_count = int(sys.argv[4])
    out_folder = sys.argv[5]
    assemblies_dir = sys.argv[2]
    substract = int(sys.argv[6])
    nr_of_sets = int(sys.argv[7])
    prefix = sys.argv[8]
    file_list = [os.path.join(assemblies_dir, file) for file in os.listdir(assemblies_dir)
                          if os.path.isfile(os.path.join(assemblies_dir, file))]

    # Run a core analysis for all sample
    simple_snp = SimpleParSNP()
    simple_snp.set_dist(dist_val)
    simple_snp.set_size(21)
    simple_snp.set_reference(ref_path)
    simple_snp.set_threads(cpu_count)
    simple_snp.set_prefix("{0}_{1}".format(prefix, len(file_list)))
    simple_snp.add_files(file_list)
    simple_snp.run_parsnp(out_folder, False, False)
    # Delete xmfa file
    os.remove(os.path.join(out_folder, "{0}_{1}.xmfa".format(prefix, len(file_list))))
