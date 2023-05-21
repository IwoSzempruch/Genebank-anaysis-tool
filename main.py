import os
from Bio import SeqIO

# Prompt for folder path
folder_path = input("Enter the folder path: ")

# Prompt for search phrase
search_phrase = input("Enter the search phrase: ")

# Create output folder
output_folder = os.path.join(folder_path, "output")
os.makedirs(output_folder, exist_ok=True)

# Iterate over each file in the input folder
for file_name in os.listdir(folder_path):
    # Check if the file is a GenBank file
    if file_name.endswith(".gb") or file_name.endswith(".gbk"):
        # Get the full file path
        file_path = os.path.join(folder_path, file_name)

        # Create the output file path
        output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_output.txt")

        # Open the output file
        with open(output_file, 'w') as output:
            # Iterate over each record in the input file
            for record in SeqIO.parse(file_path, 'genbank'):
                # Initialize a set to store the found gene values
                found_genes = set()

                # Iterate over each feature in the record
                for feature in record.features:
                    # Check if the feature contains the search phrase in the product qualifier
                    if 'product' in feature.qualifiers and search_phrase in feature.qualifiers['product'][0]:
                        gene_value = feature.qualifiers['gene'][0]

                        # Check if the gene value has been previously found
                        if gene_value not in found_genes:
                            found_genes.add(gene_value)

                            # Write information about the gene
                            output.write("Gene:\n")
                            output.write(f"/gene={gene_value}\n")
                            if 'note' in feature.qualifiers:
                                output.write(f"/note={feature.qualifiers['note'][0]}\n")
                            if 'db_xref' in feature.qualifiers:
                                output.write(f"/db_xref={feature.qualifiers['db_xref'][0]}\n")
                            output.write("\n")

                            # Write information about the mRNA
                            output.write("mRNA:\n")
                            output.write(f"/gene={gene_value}\n")
                            if 'product' in feature.qualifiers:
                                output.write(f"/product={feature.qualifiers['product'][0]}\n")
                            if 'transcript_id' in feature.qualifiers:
                                output.write(f"transcript_id={feature.qualifiers['transcript_id'][0]}\n")
                            if 'note' in feature.qualifiers:
                                output.write(f"mRNA note: {feature.qualifiers['note'][0]}\n")
                            output.write("\n")

                            # Iterate over each feature again to find CDS features with the same gene value
                            for cds_feature in record.features:
                                if cds_feature.type == 'CDS' and 'gene' in cds_feature.qualifiers and cds_feature.qualifiers['gene'][0] == gene_value:
                                    # Write information about the protein (CDS)
                                    output.write("Protein (CDS):\n")
                                    output.write(f"/gene={cds_feature.qualifiers['gene'][0]}\n")
                                    if 'note' in cds_feature.qualifiers:
                                        output.write(f"Protein note: {cds_feature.qualifiers['note'][0]}\n")
                                    if 'product' in cds_feature.qualifiers:
                                        output.write(f"/product={cds_feature.qualifiers['product'][0]}\n")
                                    if 'protein_id' in cds_feature.qualifiers:
                                        output.write(f"/protein_id={cds_feature.qualifiers['protein_id'][0]}\n")
                                    if 'translation' in cds_feature.qualifiers:
                                        output.write(f"/translation={cds_feature.qualifiers['translation'][0]}\n")
                                    output.write("\n")

                            output.write("=" * 50 + "\n")  # Add a separator between features

            # Print the number of genes found in the input file
            print(f"{file_name}, genes found: {len(found_genes)}")

# Print the success message after creating the output folder
print("Output folder created successfully.")
