from intake import intake_pdf, clear_index
from query import query_pinecone

pdf_list = ["assets/team_building.pdf"]  # ["assets/workplace_psychology.pdf"]

# clear_index()

for pdf in pdf_list:
    intake_pdf(pdf)

# results = query_pinecone("Name the five dimensions of power.")

# print(results)
