import unit_convertor
def main():
    print("UNIT CONVERTER FOR LENGTH AND WEIGHT")

    while True:
        category = input("enter category(length/weight) or 'exit' to quit: ")
        if category == 'exit':
            break

        try:
            value = float(input("enter value: "))
            from_unit = input("enter the unit to convert from: ").lower()
            to_unit = input("enter the unit to convert to: ").lower()

            if category == 'length':
                result = unit_convertor.convert_length(value , from_unit , to_unit)
                print(f"{value}{from_unit} is equal to {result}{to_unit}")
            elif category == 'weight':
                result = unit_convertor.convert_weight(value , from_unit , to_unit)
                print(f"{value} {from_unit} is equal to {result}{to_unit}")
            else:
                print("Invalid Category")
        except ValueError as e:
            print(f"error: {e}. Please enter valid inputs")
        except Exception as e:
            print(f"An unexpected erroe occurred: {e}")
        print("-" * 30)
if __name__ == "__main__":
    main()

                         