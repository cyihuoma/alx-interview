#!/usr/bin/python3

def makeChange(coins, total):
        """
            Determine the fewest number of coins needed to meet the given amount total.

                Args:
                        coins (list): A list of the values of the coins in your possession.
                                total (int): The total amount to meet.

                                    Returns:
                                            int: Fewest number of coins needed to meet the total.
                                                         If total is 0 or less, return 0.
                                                                      If total cannot be met by any number of coins, return -1.
                                                                          """
                                                                              if total <= 0:
                                                                                          return 0
                                                                                          if not coins:
                                                                                                      return -1

                                                                                                      # Sort coins in descending order
                                                                                                          coins.sort(reverse=True)
                                                                                                              change = 0

                                                                                                                  for coin in coins:
                                                                                                                              count = total // coin
                                                                                                                                      change += count
                                                                                                                                              total -= coin * count
                                                                                                                                                      if total == 0:
                                                                                                                                                                      break

                                                                                                                                                                      return change if total == 0 else -1
