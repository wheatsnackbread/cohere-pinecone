from intake import intake_pdf
from query import query_pinecone

# pdf_list = ["assets/workplace_psychology.pdf"]

# for pdf in pdf_list:
# intake_pdf(pdf)

results = query_pinecone("Name the five dimensions of power.")

print(results)
