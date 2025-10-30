def valuebet_lite():
    print("\n🎯 VALUEBET FINDER – LITE EDITION v1.0\n")

    try:
        probability = float(input("👉 Your estimated probability (%): "))
        odds = float(input("👉 Bookmaker odds: "))
        stake = float(input("👉 Stake (€): "))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
        return

    p = probability / 100
    break_even_odds = 1 / p
    is_value_bet = odds > break_even_odds
    profit = (stake * odds) - stake
    loss = -stake
    expected_value = (p * profit) + ((1 - p) * loss)
    kelly = ((odds * p) - (1 - p)) / odds
    kelly_stake = stake * kelly if kelly > 0 else 0

    print("\n📊 RESULTS:")
    print(f"- Break-even odds: {break_even_odds:.2f}")
    print(f"- Value bet: {'YES ✅' if is_value_bet else 'NO ❌'}")
    print(f"- Expected value (EV): {expected_value:.2f} €")
    print(f"- Kelly stake: {kelly_stake:.2f} €")

    print("\n💡 RECOMMENDATION:")
    if is_value_bet and expected_value > 0:
        print("✅ BET – value bet detected.")
    else:
        print("❌ DO NOT BET – not profitable.")

valuebet_lite()

