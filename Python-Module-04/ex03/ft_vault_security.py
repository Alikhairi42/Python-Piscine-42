#!/usr/bin/env python3


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)

        if action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")

        return (False, "Invalid action")

    except IOError as err:
        return (False, str(err))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("ali.txt")
    print(result)

    print("\nReading an existing file:")
    result = secure_archive("test.txt")
    print(result)

    print("\nWriting to a new file:")
    result = secure_archive(
        "new_archive.txt",
        "write",
        "Secret archive data"
    )
    print(result)



if __name__ == "__main__":
    main()
