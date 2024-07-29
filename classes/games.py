import random
from.magic import spell

class person:
    def __init__(self,name,hp,mp,atk,df,magic,item):
        self.hp=hp
        self.maxhp=hp
        self.mp=mp
        self.maxmp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.item=item
        self.action=["Attack","magic","Item"]
        self.name=name

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)


    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp

    def heal(self,dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp

    def get_hp(self):
        return self.hp
    def get_maxhp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_maxmp(self):
        return self.maxmp
    def reduce_mp(self,cost):
        self.mp-=cost
    def get_spell_name(self,i):
        return self.magic[i]["name"]
    def get_spell_cost(self,i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i=1
        print("\n")
        print("   "+self.name)
        print("   Action")
        for items in self.action:
            print("      "+str(i)+":",items)
            i+=1

    def choose_spell(self):
        i=1
        print("\n")
        print("   Magic")
        for spell in self.magic:
            print("      "+str(i)+":",spell.name,"cost:",str(spell.cost))
            i+=1

    def choose_Items(self):
        i=1
        print("\n")
        print("   Items")
        for items in self.item:
            print("      "+str(i)+":",items["item"].name,":",items["item"].description,"x"+str(items["quantity"]))
            i+=1

    def choose_target(self,enemies):
        i=1
        print("---------TARGET---------")
        for enemy in enemies:
            if enemy.get_hp()!=0:
                print("          "+str(i)+".",enemy.name)
                i+=1
        choice=int(input("Choose target"))-1
        return choice

    def get_stats(self):
        hp_bar=""
        hp_bar_ticks=int((self.hp/self.maxhp)* 100/4)
        while hp_bar_ticks:
            hp_bar+="█"
            hp_bar_ticks-=1
        while len(hp_bar)<25:
            hp_bar+=" "

        mp_bar = ""
        mp_bar_ticks = int((self.mp / self.maxmp) * 100 / 10)
        while mp_bar_ticks:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_strings=str(self.hp)+"/"+str(self.maxhp)
        current_hp=""
        if len(hp_strings)<9:
            decreased=9-len(hp_strings)
            while decreased:
                current_hp+=" "
                decreased-=1
            current_hp+=hp_strings
        else:
            current_hp=hp_strings

        mp_strings = str(self.mp)+"/"+str(self.maxmp)
        current_mp = ""
        if len(mp_strings) < 7:
            decreased = 7 -len(mp_strings)
            while decreased:
                current_mp += " "
                decreased -= 1
            current_mp += mp_strings
        else:
            current_mp = mp_strings
        print("                 _________________________                   __________")
        print(self.name+" "+current_hp+"|"+hp_bar+"|          "+current_mp+"|"+mp_bar+"|")

    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar_ticks = int((self.hp / self.maxhp) * 100 / 2)
        while hp_bar_ticks:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_strings = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_strings) < 11:
            decreased = 11 - len(hp_strings)
            while decreased:
                current_hp += " "
                decreased -= 1
            current_hp += hp_strings
        else:
            current_hp = hp_strings
        print("                 __________________________________________________")
        print(self.name + " " + current_hp + "|" + hp_bar + "|          ")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        mg_damage = spell.generate_spelldamage()
        pct=self.mp/self.maxmp *100

        if self.mp<spell.cost or spell.type=="white" and pct>50:
            self.choose_enemy_spell()
        else:
            return spell,mg_damage
