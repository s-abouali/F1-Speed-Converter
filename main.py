print("=" * 50)
print("        🏎️ F1 SPEED CONVERTER")
print("=" * 50)

print("\nChoose the input unit:")
print("1. km/h")
print("2. mph")
print("3. m/s")
print("4. knots")

choice = input("\nYour choice: ")

try:
    speed = float(input("Enter speed: "))

    if speed < 0:
        print("Speed cannot be negative.")
        exit()

    # Convert everything to km/h first
    if choice == "1":
        kmh = speed

    elif choice == "2":
        kmh = speed * 1.609344

    elif choice == "3":
        kmh = speed * 3.6

    elif choice == "4":
        kmh = speed * 1.852

    else:
        print("Invalid choice.")
        exit()

    # Convert km/h into all other units
    mph = kmh / 1.609344
    ms = kmh / 3.6
    knots = kmh / 1.852

    print("\n" + "=" * 50)
    print("              RESULTS")
    print("=" * 50)

    print(f"\n🏎️ km/h:   {kmh:.2f}")
    print(f"🇺🇸 mph:    {mph:.2f}")
    print(f"⚡ m/s:     {ms:.2f}")
    print(f"🌊 knots:   {knots:.2f}")

    # F1-style analysis
    print("\n" + "-" * 50)
    print("              F1 ANALYSIS")
    print("-" * 50)

    if kmh >= 300:
        print("🔥 EXTREME SPEED — F1 top-speed territory!")

    elif kmh >= 250:
        print("🏎️ HIGH SPEED — serious racing pace!")

    elif kmh >= 200:
        print("🏁 RACING SPEED!")

    elif kmh >= 100:
        print("🚗 Road-car territory.")

    else:
        print("🐌 That's slower than an F1 car!")

except ValueError:
    print("Please enter a valid number.")

print("\n" + "=" * 50)
print("          CONVERSION COMPLETE")
print("=" * 50)
