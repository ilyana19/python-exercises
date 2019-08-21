class Player:
  def __init__(self, gold = 0, hp = 10, lives = 5):
    self.lives = lives
    self.gold = gold
    self.hp = 10

  def __str__(self):
    return (
      "----------------------\n"
      f"Lives: {self.lives}\n"
      f"HP: {self.hp}\n"
      f"Gold: {self.gold}\n"
      "----------------------"
    )

  def level_up(self):
    self.lives += 1
    return f"You have {self.lives} lives."

  def collect_treasure(self):
    self.gold += 1

    if self.gold % 10 == 0:
      self.level_up()
    
    return f"Player collected {self.gold} gold."

  def battle(self, damage):
    self.hp -= damage
    print(f"You took {damage} damage.")

    if self.hp < 1:
      self.lives -= 1
      self.hp = 10
      print(f"You died. You now have {self.lives} lives left.")

    if self.lives == 0:
      self.restart()
  
  def restart(self):
    self.lives = 5
    self.hp = 10
    self.gold = 0
    print("Gameover")

player = Player()
print(player)

for i in range(5):
  # print(player.collect_treasure())
  player.battle(10)
  print(player)


print(player.collect_treasure())
print(player)
