def calculate_output(input_value):
    # Given points
    x1, y1 = 3.5, 400
    x2, y2 = 3.3, 1488

    # Calculate slope
    slope = (y2 - y1) / (x2 - x1)

    # Calculate output using point-slope form: y - y1 = m * (x - x1)
    output = slope * (input_value - x1) + y1

    return output


def main():
    input_value = float(input("Enter a floating-point number: "))
    output = calculate_output(input_value)
    print("Output:", output)


if __name__ == "__main__":
    main()
