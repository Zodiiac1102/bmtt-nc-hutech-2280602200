import base64

def main():
    try:
        with open("data.txt", "r") as file:
            encoded_string = file.read()
    

            decoded_bytes = base64.b64decode(encoded_string.encode("utf-8"))
            decoded_string = decoded_bytes.decode("utf-8")

        print("Chuỗi sau khi giải mã:", decoded_string)
    except Exception as e:
        print("Lỗi:", str(e))

if __name__ == "__main__":
    main()
