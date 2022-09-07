
from http import client
import discord
from discord.ext import commands, tasks
import time
import datetime
import requests
import sched

s = sched.scheduler(time.time, time.sleep)

dms = []

quotes = {"1": {"author": "John Doe", "quote": "et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra", "tip": "at augue eget arcu dictum varius duis at consectetur lorem donec massa sapien faucibus et"},
    "99": {"author": "Harry Emerson Fosdick", "quote": "One must have the adventurous daring to accept oneself as a bundle of possibilities.", "tip": "If just 25% \of U.S. families used 10 fewer plastic bags a month, we would save over 2.5 billion bags a year."},
            "2": {"author": "Anthony J. D'Angelo", "quote": "Without a sense of caring, there can be no sense of community.",  "tip": "Be assertive, not aggressive."},
            "3": {"author": "E.V. Lucas", "quote": "I'm a believer in punctuality, though it makes me very lonely.",  "tip": "When 13,000 people walking 30 minutes a day were tracked for eight years, a study found their risk for premature death was much lower than those who rarely exercised."},
            "4": {"author": "Alan Simpson", "quote": "If you have integrity, nothing else matters. If you don't have integrity, nothing else matters.",  "tip": "Humans can smell the most minuscule amount of skunk spray, even from a mile away."},
            "5": {"author": "Jonathan Moyo", "quote": "Loyalty is a 24-hour prposition, 24/7. It's not a part-time job.",  "tip": "Tropical forests fill the world's medicine cabinets: medicine produced in tropical forests grosses $30 billion a year!"},
            "6": {"author": "Benjamin Franklin", "quote": "The doors of wisdom are never shut.",  "tip": "Life is a product of your decisions, not your conditions. Don't let circumstances define you. Be proactive; use your freedom to make choices."},
            "7": {"author": "Kahlil Gibran", "quote": "Truth is a deep kindness that teaches us to be content in our everyday life and share with the people the same happiness.",  "tip": "Water exercise is one of the best nonimpact fitness activities. It encompasses cardiovascular fitness, muscular strength, endurance, and flexibility, and it can help reduce body fat."},
            "8": {"author": "Isaac Asimov", "quote": "No sensible decision can be made any longer without taking into account not only the world as it is, but the world as it will be.",  "tip": "Think of any number. Multiply that number by 3. Add 45 to the result. Double the result. Divide the answer by 6. Subtract your original number from the answer. The answer will always be 15. Try it!"},
            "9": {"author": "Bertolt Brecht", "quote": "Everyone needs help from everyone.",  "tip": "The U.S. EPA resports that in 2018, newspapers had a recycling rate of 64.8 percent."},
            "10": {"author": "Knute Rockne", "quote": "One man practicing sportsmanship is better than 100 teaching it.",  "tip": "The key to listening is with the eyes and the heart. Great listeners listen wholeheartedly and mirror back what the individual is telling them. Listen with the intent to understand, not reply."},
            "11": {"author": "Thomas A. Edison", "quote": "Opportunity is missed by most people because it is dressed in overalls and looks like work.",  "tip": " Avoiding foods containing high-fructose forn syrup is a sure way to cut back on excess calories from sugar and likely to lead you to healthier food choices."},
            "12": {"author": "Calvin Coolidge", "quote": "There is no development physically or intellectuall without effor, and effort means work.",  "tip": "Ford Motor Co. indicates that 85% \of every vehicle is recyclable"},
            "13": {"author": "Henry S. Truman", "quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us.",  "tip": "We don't know who we impact with our words and actions. Be aware that you could have a lasting impact on those around you. How do you want to be remembered?"},
            "14": {"author": "Vince Lombardi", "quote": "The achievements of an organization are the results of the combined effor of each individual.",  "tip": "Not only is jumping rope a great cardiovascular alternative to your usual aerobic workout, jumping rope can increase body awareness and develop better hand and foot coordination."},
            "15": {"author": "Eleanor Roosevelt", "quote": "It is not fair to ask of others what you are not willing to do yourself.",  "tip": "Small vs. big: A bucket full of water contains more atoms than there are bucketfuls of water in the Atlantic Ocean."},
            "16": {"author": "Cecil B. DeMille", "quote": "The person who makes a success of living is the one who sees his goal steadily and aims for it unswervingly. That is dedication.",  "tip": "Americans use between 70 an 100 gallons of water indoors each day."},
            "17": {"author": "Bertrand Russell", "quote": "The only thing that will redeem mankind is cooperation.",  "tip": "Synergy is people working together for a common goal, which builds community and strength among people. When have you participated in a synergistic group?"},
            "18": {"author": "St. Augustine", "quote": "Patience is the companion of wisdom.",  "tip": "Move more. make it a daily challenge to find ways to move your bodu. Instead of the elevator, take the stairs. Walk your dog, toss balls with friends, mow the lawn. Anything that moves your limbs is not only a fitness tool, it's a stress buster."},
            "19": {"author": "Euripides", "quote": "Character is a stamp of good repute on a person.", "tip": "Polar bear fur is so effective an insulator that infrared (heat-seeing) cameras can barely detect them. The hairs are hollow to provide extra insulation."},
            "20": {"author": "Terry Josephson", "quote": "If you don't appreciate it, you don't deserve it.", "tip": "About 20% \of the world's oxygen is produced by the Amazon rainforest"},
            "21": {"author": "Faith Baldwin", "quote": "Character builds slowly, but it can be torn down with incredible switfness.", "tip": "In teamwork and innovation, both differences and similarities bring value."},
            "22": {"author": "Josh Billings", "quote": "One of the greatest victories you can gain over someone is to beat him at politeness.", "tip": "The U.S. Department of Energy reports that wind energy supplied more than 8% \of total U.S. electricity in 2020."},
            "23": {"author": "Benjamin Franklin", "quote": "Energy and persistence conquer all things.", "tip": "Be a methodical organizer. Discover what works for you and stick to it."},
            "24": {"author": "Ruth Gordon", "quote": "Courage is like a muscle strengthened by its use.", "tip": "Pilates, tai chi, and yoga exercise the mind, the spirit, and the body."},
            "25": {"author": "Franklin P. Jones", "quote": "Bravery is being the only one who knows you're afraid.", "tip": "The burning sensation we get from chili peppers is caused by a chemical called capsaicin."},
            "26": {"author": "Charles F. Kettering", "quote": "Knowing is not understanding. There is a great difference between knowing and understanding; you can know a lot about something and not really understand it.", "tip": "About 2,500 gallons of water are needed to produce every pound of beef."},
            "27": {"author": "Arnold H. Glasow", "quote": "Success is simple. Do what's right, the right way, at the right time.", "tip": "Think small. Break up larger tasks into smaller ones that are more manageable."},
            "28": {"author": "Calvin Coolidge", "quote": "Patriotism is easy to understand in America; it means looking out for yourself by looking out for your country.", "tip": "Stay active throughout your day. Walk bike, dance, keep moving - that can burn more calories than an intense gym workout."},
            "29": {"author": "Mother Teresa", "quote": "Kind words can be short and easy to speak, but their echoes are truly endless.", "tip": "Your body is made of 65% \oxygen, 18% \carbon, 10% hydrogen, 3% nitrogen, 1.5% \calcium, 1% phosphorus, and 1.5% \of six other elements."},
            "30": {"author": "Les Brown", "quote": "We must look for ways to be an active force in our own lives. We must take charge of our own actions.", "tip": "Lower your carbon footprint by reducing what you own. What could you do without? What useful item could be repaired or maintained to lats longer?"},
            "31": {"author": "Zig Ziglar", "quote": "Attitude is the little thing that makes the big difference.", "tip": "Keep an idea log with you for larger projects, such as a research paper or essay. You never know when inspiration may strike you."},
            "32": {"author": "George Bernard Shaw", "quote": "Better keep yourself clean and bright. You are the window through whcih you must see the world.", "tip": "Dieting, fasting, and other \"quick fixes\" won't work. Think of permanent, positive changes to your diet and ensure for yourself a healthy, fit future."},
            "33": {"author": "Greenville Kleiser", "quote": "By constant self-discipline and self-control you can develop greatness of character.", "tip": "When sand, soda ash, and lime are heated to very hot temperatures, they form a thick syrup, which turns into glass once cool."},
            "34": {"author": "Vince Lombardi", "quote": "Individual commitment to a group effort - that is what makes a team work, a company work, a society work, a civilization work.", "tip": "Paper towels and napkins are convenient but a poor choice for the environment. Use cloth napkins and recycle old T-shirts as rags instead."},
            "35": {"author": "Mignon Mclaughlin", "quote": "A sense of humor is a major defense against minor troubles.", "tip": "Take advantage of every resource. Make sure that you are using your time most effectively by getting help from your teachers or other students."},
            "36": {"author": "Marva Collins", "quote": "Determination and perseverance move the world; thinking that others will do it for you is a sure way to fail.", "tip": "According to researchers, among the most beneficial fruits and vegetables known to man: prunes, raisins, blueberries, blackberries, kale, strawberries, and spinach."},
            "37": {"author": "William A. Ward", "quote": "Curiosity is the wick in the candle of learning.", "tip": "Cordyceps fungi are remarkable because of how they prey upon insect life. Look them up!"},
            "38": {"author": "Henry Wadsworth Longfellow", "quote": "Perserverance is a great element of success. If you only knock long enough and loud enough at the gate, you are sure to wake up somebody.", "tip": "If you can, buy it in bulk. This saves you money and helps the environment by reducing packaging."},
            "39": {"author": "Joshua J. Marine", "quote": "Challenges are what make life interesting; overcoming them is what makes life meaningful.", "tip": "Don't wait. Do it now. Get organized, get ready, and get control. Success is waiting for you!"},
            "40": {"author": "Peter F. Drucker", "quote": "Unless commitment is made, there are only promises and hopes... but no plans.", "tip": "The body is an engine; feed it the right fuel! How much do you exercise? How much do you currently eat? What foods can help you reach your goals? Changing the way you think about food and your body can \"tune up\" your daily performance."},
            "41": {"author": "Confucius", "quote": "The superior man thinks always of virtue; the common man thinks of comfort.", "tip": "By age 8, over half of children (52%) have had a cavity in their primary (baby) teeth, according to the Centers for Disease Control and Prevention."},
            "42": {"author": "Cher", "quote": "I can trust my friends. These people force me to examine myself, encourage me to grow.", "tip": "Turning down your central heating thermostat by 1 degree can cut fuel consumption by as much as 10%."},
            "43": {"author": "Salvador Dalí", "quote": "At the age of 6, I wanted to be a cook. At 7, I wanted to be Napoleon. And my ambition has been growing steadily ever since.", "tip": "Plan for fun as well as work."},
            "44": {"author": "Martin Luther King Jr.", "quote": "The function of education is to teach one to think intensively and to think critically. Intelligence plus character - that is the goal of true education.", "tip": "Stay hydrated! The human body is made up of 60% water, and that water is essential to your daily functions."},
            "45": {"author": "Thomas Jefferson", "quote": "I believe... that every human mind feels pleasure in doing good to another.", "tip": "A full rainbow is actually a complete circle, but from the ground, we see only part of it. From an ariplane, in the right conditions, one can see an entire circular rainbow."},
            "46": {"author": "Nicolas Boilleau-Despréaux", "quote": "Honor is like an island, rugged and without a beack; once we have left it, we can never return.", "tip": "Oceans make up 70% \of Earth, yet over 80% \of the world's oceans are still unexplored."},
            "47": {"author": "John Evelyn", "quote": "Friendship is the golden thread that ties the heart of all the world.", "tip": "Working with others is a challenge. Working well with others is a leadership trait."},
            "48": {"author": "Charlotte Brontë", "quote": "True enthusiasm is a fine feeling whose flash I admire wherever I see it.", "tip": "Listen to your body while you eat! Being in tune with your body helps you identify when you're full and keeps you from overeating and feeling uncomfortable."},
            "49": {"author": "H. Jackson Brown Jr.", "quote": "Talent without discipline is like an octopus on roller skates. There's plenty of movement, but you never know if it's going to be forward, backwards, or sideways.", "tip": "The Great Barrier Reef is the largest living structure on earth, stretching 1,429 miles and covering an area of more than 133,000 square miles!"},
            "50": {"author": "Dwight L. Moody", "quote": "Character is what you are in the dark.", "tip": "Say no to plastic bags! Plastic bags stay around a long time after you throw them away. They actually take up to 1,000 years to decompose!"},
            "51": {"author": "Tony Robbins", "quote": "Stay committed to your decisions, but stay flexible in your approach.", "tip": "Harness the power of habit and routine! Set a specific time period for each task you want to accomplish."}
}

class daily_quote(commands.Cog):
    def __init__ (self, client):
        self.client = client
        self.daily_quote_tips.start()
        
    def cog_unload(self):
        self.daily_quote_tips.cancel()



    @commands.command(help = "toggle whether you want to receive daily quotes and facts in your dms, argument type: Boolean (true/false)")
    async def quote_dm(self, ctx, state):
        state = state.lower()
        if state != "true" and state != "false":
            await ctx.send("that is not a boolean (true/false)")
        else:
            try:
                db = self.client.get_channel(1016103072147185697)
                dms = await db.history(limit = 80).flatten()
                if dms:
                    for msg in dms:
                        if state == "true" and ctx.author.id != int(msg.content):    
                            await db.send(ctx.author.id)
                            await ctx.send("You will now receive daily quotes.")
                            return()
                        elif state == "true" and ctx.author.id == int(msg.content):
                            await ctx.send("You're already receiving daily quotes.")
                            return()
                        elif state == "false" and ctx.author.id == int(msg.content):
                            await ctx.send("You will no longer receive daily quotes.")
                            await msg.delete()
                            return()
                        else:
                            pass
                    await ctx.send("You were never going to receive quotes in the first place. Nothing has changed.")
                elif state == "true":
                    await db.send(ctx.author.id)
                    await ctx.send("You will now receive daily quotes.")
                else:
                    await ctx.send("You were never going to receive quotes in the first place. Nothing has changed.")

            except Exception as e:
                await ctx.send(e)
                print(e)
            
        

    @tasks.loop(seconds = 300)
    async def daily_quote_tips(self):
        try:
            channel = self.client.get_channel(896748385724432415)
            db = self.client.get_channel(1016103072147185697)
            dms = await db.history(limit = 80).flatten()
            this_day = datetime.datetime.strptime(str(datetime.datetime.today().strftime('%d-%m-%Y')), "%d-%m-%Y").timetuple().tm_yday - 247
            send_time = time.mktime(datetime.datetime.strptime(str(datetime.datetime.today().strftime('%d-%m-%Y')),"%d-%m-%Y").timetuple())
            if datetime.datetime.today().timetuple().tm_hour < 6:
                send_time = time.mktime(datetime.datetime.strptime(str(datetime.datetime.today().strftime('%d-%m-%Y')),"%d-%m-%Y").timetuple()) + 21600
            else:
                send_time = time.mktime(datetime.datetime.strptime(str(datetime.datetime.today().strftime('%d-%m-%Y')),"%d-%m-%Y").timetuple()) + 108000

            async def send_quote(quote_num):
                quote_num = str(quote_num)
                data = (f"""__Quote of the day:__ \n**"{quotes[quote_num]['quote']}"**  *- {quotes[quote_num]['author']}* \n \n__Tip/Fact of the day:__ \n**{quotes[quote_num]['tip']}**""")
                for i in dms:
                    print(i)
                    person = self.client.get_user(int(i.content))
                    await person.send(data)
                await channel.send(data)
            #s.enterabs(send_time, 1, await send_quote(this_day))
            #await s.run()
            if abs(send_time - time.time()) < 301:
                await send_quote(this_day)
        except Exception as e:
            await channel.send(e)
            print(e)
    
    @daily_quote_tips.before_loop
    async def before_daily_quote_tips(self):
        print('Getting quotes') 
        await self.client.wait_until_ready()


def setup(client): 
    client.add_cog(daily_quote(client))
