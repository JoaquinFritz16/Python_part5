def DiscountCalc():
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = original_price - (discount_percentage / 100 * original_price)

    print(f"The final price after a discount of {discount_percentage}% is: ${final_price:.2f}")

if __name__ == "__main__":
    DiscountCalc()
