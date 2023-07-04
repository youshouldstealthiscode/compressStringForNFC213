import io
import pyhuffman
import nfcpy

def is_utf8(data):
  """Checks if the given data is UTF-8 encoded."""
  return io.TextIOWrapper(io.BytesIO(data)).encoding == "utf-8"

def encode_huffman(data):
  """Encodes the given data using Huffman coding."""
  tree = pyhuffman.build_tree(data)
  encoded_data = pyhuffman.encode(data, tree)
  return encoded_data

def write_to_nfc_tag(data):
  """Writes the given data to an NFC213 tag."""
  device = nfcpy.Nfc()
  device.connect()
  device.write(data)
  device.close()

def main():
  data = "hello world"

  # Check if the data is UTF-8 encoded.
  if not is_utf8(data):
    data = data.encode("utf-8")

  # Encode the data using Huffman coding.
  encoded_data = encode_huffman(data)

  # Write the encoded data to the NFC tag.
  write_to_nfc_tag(encoded_data)

if __name__ == "__main__":
  main()
