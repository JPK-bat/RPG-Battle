from classes.games import person
from classes.magic import spell
from classes.inventory import Item
import random


#Create Black Magic
fire=spell("fire",10,60,"black")
thunder=spell("thunder",11,65,"black")
blizzard=spell("blizzard",12,70,"black")
quake=spell("quake",13,75,"black")
meteor=spell("meteor",14,80,"black")

#create White magic
cure=spell("cure",11,50,"white")

#Inventory
portion=Item("potion","potion","heals 50 HP",50)
hipotion=Item("hi-potion","potion","heals 100 HP",100)
superpotion=Item("super-potion","potion","heals 500 HP",500)
elixer=Item("elixer","elixer","restores HP/MP of one party",9999)
superelixer=Item("super-elixer","elixer","restores all party's HP/MP",10000)

grenade=Item("Grenade","attack","deals 50 damage",50)


player_spells=[fire,thunder,blizzard,quake,meteor,cure]
enemy_spell=[fire,meteor,cure]
player_items=[{"item":portion, "quantity":15},
              {"item":hipotion, "quantity":5},
              {"item":superpotion, "quantity":5},
              {"item":elixer, "quantity":2},
              {"item":superelixer, "quantity":3},
              {"item":grenade,"quantity":3}]


#create players
player1=person("batsy:",2000,100,65,40,player_spells,player_items)
player2=person("supes:",2000,100,65,40,player_spells,player_items)
player3=person("women:",2000,100,65,40,player_spells,player_items)

players=[player1,player2,player3]
enemy1=person("Lex:",10000,70,50,45,enemy_spell,[])
enemy2=person("jok:",10000,70,50,45,enemy_spell,[])
enemy3=person("ari:",10000,70,50,45,enemy_spell,[])

enemies=[enemy1,enemy2,enemy3]

run=True

while run:
       print("========================")
       print("\n\n")
       print("NAME             HP                                          MP")
       for player in players:
           player.get_stats()
       print("\n")
       for enemy in enemies:
            enemy.get_enemy_stats()
       for player in players:
           player.choose_action();
           choice=int(input("   choose action:"))
           index=choice-1
           if index==0:
                  dmg=player.generate_damage();
                  enemy=player.choose_target(enemies)
                  enemies[enemy].take_damage(dmg)
                  print("   you attacked for "+str(dmg)+" points of damage")
                  if enemies[enemy].get_hp()==0:
                      print(enemies[enemy]+" has dies ")
                      del enemies[enemy]
           elif index==1:
                  player.choose_spell();
                  mg_choice=int(input("   choose spell:"))-1
                  spell=player.magic[mg_choice]
                  enemy = player.choose_target(enemies)
                  mg_damage=spell.generate_spelldamage()
                  current_mp=player.get_mp()
                  if spell.cost>current_mp:
                         print("NOT ENPOUGH")
                         continue
                  player.reduce_mp(spell.cost)
                  if spell.type=="white":
                      player.heal(mg_damage)
                      print("\n"+"   "+spell.name+" heals "+str(mg_damage))
                  elif spell.type=="black":
                    enemies[enemy].take_damage(mg_damage)
                    print("   "+spell.name+"deals"+str(mg_damage)+"points of damage to"+enemies[enemy].name)
                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy] + " has dies ")
                        del enemies[enemy]
           elif index==2:
               player.choose_Items();
               item_choice=int(input("   choose_items:"))-1
               item=player.item[item_choice]["item"]
               enemy = player.choose_target(enemies)
               if player.item[item_choice]["quantity"]==0:
                   print(item.name+" NONE LEFT-------")
                   continue
               player.item[item_choice]["quantity"]-=1

               if item.type=="potion":
                   player.heal(item.prop)
                   print("\n"+"   "+item.name+" heals for "+str(item.prop))
               elif item.type=="elixer":
                   if item.name=="super-elixer":
                       for i in players:
                           i.hp=i.maxhp
                           i.mp=i.maxmp
                   else:
                        player.hp=player.maxhp
                        player.mp=player.maxmp
                   print("\n"+"Fully restored HP/MP")
               elif item.type=="attack":
                   enemies[enemy].take_damage(item.prop)
                   print("\n"+"   "+item.name+"deals with"+str(item.prop)+"damage to"+enemies[enemy].name)
                   if enemies[enemy].get_hp() == 0:
                       print(enemies[enemy] + " has dies ")
                       del enemies[enemy]


       for enemy in enemies:
           enemy_choice=random.randrange(0,3)
           if enemy_choice==0:
               target=random.randrange(0,3)
               dmg = enemy.generate_damage();
               players[target].take_damage(dmg)
               print(enemy.name+"  attacked "+players[target].name+ " for " + str(dmg) + " points of damage")

           elif enemy_choice==1:
               spell, mg_damage=enemy.choose_enemy_spell()
               enemy.reduce_mp(spell.cost)
               target = random.randrange(0, 3)
               if spell.type == "white":
                   enemy.heal(mg_damage)
                   print("\n" + "   " + spell.name + " heals " + str(mg_damage))
               elif spell.type == "black":
                   players[target].take_damage(mg_damage)
                   print("   " + spell.name + "deals" + str(mg_damage) + "points of damage to" + players[target].name)
                   if players[target].get_hp() == 0:
                       print(players[target] + " has dies ")
                       del players[target]

       defeated_enemy=0
       defeated_player=0

       for enemy in enemies:
           if enemy.get_hp()==0:
               defeated_enemy+=1

       for player in players:
            if player.get_hp()==0:
                defeated_player+=1

       if defeated_enemy==2:
              print("****YOU WIN!****")
              run=False
       elif defeated_player==2:
              print("****YOU LOST****")
              run=False
