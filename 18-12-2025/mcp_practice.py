from pydantic import Field
from mcp.server.fast import Fastmcp

mcp = Fastmcp("DocumentMCP", log_level="ERROR")

@mcp.tool(
    name="read_document",
    description="Reads the content of a document and returns it as a string"
)

def read_document(
    doc_id: str = Field(..., description="The unique identifier of the document to read")
    if doc_id not in doc:
        raise ValueError("Document not found")
)

@mcp.tool(
    name="write_document",
    description="Writes content to a document identified by its unique identifier"
)   
def write_document(
    doc_id: str = Field(..., description="The unique identifier of the document to write to"),
    content: str = Field(..., description="The content to write into the document")
):
    if doc_id not in doc:
        raise ValueError("Document not found")
    doc[doc_id] = content
    return "Document updated successfully"