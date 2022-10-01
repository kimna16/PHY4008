Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #text
>>> text1="Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed. A yellow dressinggown, ungirdled, was sustained gently behind him on the mild morning air. He held the bowl aloft and intoned: Introibo ad altare Dei. Halted, he peered down the dark winding stairs and called out coarsely: Come up, Kinch! Come up, you fearful jesuit! Solemnly he came forward and mounted the round gunrest. He faced about and blessed gravely thrice the tower, the surrounding land and the awaking mountains. Then, catching sight of Stephen Dedalus, he bent towards him and made rapid crosses in the air, gurgling in his throat and shaking his head. Stephen Dedalus, displeased and sleepy, leaned his arms on the top of the staircase and looked coldly at the shaking gurgling face that blessed him, equine in its length, and at the light untonsured hair, grained and hued like pale oak. "
>>> text2="Buck Mulligan peeped an instant under the mirror and then covered the bowl smartly. Back to barracks! he said sternly. He added in a preacher’s tone: For this, O dearly beloved, is the genuine Christine: body and soul and blood and ouns. Slow music, please. Shut your eyes, gents. One moment. A little trouble about those white corpuscles. Silence, all. He peered sideways up and gave a long slow whistle of call, then paused awhile in rapt attention, his even white teeth glistening here and there with gold points. Chrysostomos. Two strong shrill whistles answered through the calm. Thanks, old chap, he cried briskly. That will do nicely. Switch off the current, will you? He skipped off the gunrest and looked gravely at his watcher, gathering about his legs the loose folds of his gown. The plump shadowed face and sullen oval jowl recalled a prelate, patron of arts in the middle ages. A pleasant smile broke quietly over his lips."
>>> 
>>> #txt1, txt2
>>> txt1=text1.split()
>>> txt2=text2.split()
>>> 
>>> txt1
['Stately,', 'plump', 'Buck', 'Mulligan', 'came', 'from', 'the', 'stairhead,', 'bearing', 'a', 'bowl', 'of', 'lather', 'on', 'which', 'a', 'mirror', 'and', 'a', 'razor', 'lay', 'crossed.', 'A', 'yellow', 'dressinggown,', 'ungirdled,', 'was', 'sustained', 'gently', 'behind', 'him', 'on', 'the', 'mild', 'morning', 'air.', 'He', 'held', 'the', 'bowl', 'aloft', 'and', 'intoned:', 'Introibo', 'ad', 'altare', 'Dei.', 'Halted,', 'he', 'peered', 'down', 'the', 'dark', 'winding', 'stairs', 'and', 'called', 'out', 'coarsely:', 'Come', 'up,', 'Kinch!', 'Come', 'up,', 'you', 'fearful', 'jesuit!', 'Solemnly', 'he', 'came', 'forward', 'and', 'mounted', 'the', 'round', 'gunrest.', 'He', 'faced', 'about', 'and', 'blessed', 'gravely', 'thrice', 'the', 'tower,', 'the', 'surrounding', 'land', 'and', 'the', 'awaking', 'mountains.', 'Then,', 'catching', 'sight', 'of', 'Stephen', 'Dedalus,', 'he', 'bent', 'towards', 'him', 'and', 'made', 'rapid', 'crosses', 'in', 'the', 'air,', 'gurgling', 'in', 'his', 'throat', 'and', 'shaking', 'his', 'head.', 'Stephen', 'Dedalus,', 'displeased', 'and', 'sleepy,', 'leaned', 'his', 'arms', 'on', 'the', 'top', 'of', 'the', 'staircase', 'and', 'looked', 'coldly', 'at', 'the', 'shaking', 'gurgling', 'face', 'that', 'blessed', 'him,', 'equine', 'in', 'its', 'length,', 'and', 'at', 'the', 'light', 'untonsured', 'hair,', 'grained', 'and', 'hued', 'like', 'pale', 'oak.']
>>> txt2
['Buck', 'Mulligan', 'peeped', 'an', 'instant', 'under', 'the', 'mirror', 'and', 'then', 'covered', 'the', 'bowl', 'smartly.', 'Back', 'to', 'barracks!', 'he', 'said', 'sternly.', 'He', 'added', 'in', 'a', 'preacher’s', 'tone:', 'For', 'this,', 'O', 'dearly', 'beloved,', 'is', 'the', 'genuine', 'Christine:', 'body', 'and', 'soul', 'and', 'blood', 'and', 'ouns.', 'Slow', 'music,', 'please.', 'Shut', 'your', 'eyes,', 'gents.', 'One', 'moment.', 'A', 'little', 'trouble', 'about', 'those', 'white', 'corpuscles.', 'Silence,', 'all.', 'He', 'peered', 'sideways', 'up', 'and', 'gave', 'a', 'long', 'slow', 'whistle', 'of', 'call,', 'then', 'paused', 'awhile', 'in', 'rapt', 'attention,', 'his', 'even', 'white', 'teeth', 'glistening', 'here', 'and', 'there', 'with', 'gold', 'points.', 'Chrysostomos.', 'Two', 'strong', 'shrill', 'whistles', 'answered', 'through', 'the', 'calm.', 'Thanks,', 'old', 'chap,', 'he', 'cried', 'briskly.', 'That', 'will', 'do', 'nicely.', 'Switch', 'off', 'the', 'current,', 'will', 'you?', 'He', 'skipped', 'off', 'the', 'gunrest', 'and', 'looked', 'gravely', 'at', 'his', 'watcher,', 'gathering', 'about', 'his', 'legs', 'the', 'loose', 'folds', 'of', 'his', 'gown.', 'The', 'plump', 'shadowed', 'face', 'and', 'sullen', 'oval', 'jowl', 'recalled', 'a', 'prelate,', 'patron', 'of', 'arts', 'in', 'the', 'middle', 'ages.', 'A', 'pleasant', 'smile', 'broke', 'quietly', 'over', 'his', 'lips.']
>>> 
>>> #capitalNum1, capitalNum2, tmp1, tmp2
>>> capitalNum1=0
>>> capitalNum2=0
>>> tmp1=[]
>>> tmp2=[]
>>> 
>>> for x in txt1:
	if x[0].isupper():
		capitalNum1+=1
		tmp1.append(x)

		
>>> for x in txt2:
	if x[0].isupper():
		capitalNum2+=1
		tmp2.append(x)

		
>>> 
>>> #Answer of No.1
>>> capitalNum1
18
>>> capitalNum2
21
>>> tmp1
['Stately,', 'Buck', 'Mulligan', 'A', 'He', 'Introibo', 'Dei.', 'Halted,', 'Come', 'Kinch!', 'Come', 'Solemnly', 'He', 'Then,', 'Stephen', 'Dedalus,', 'Stephen', 'Dedalus,']
>>> tmp2
['Buck', 'Mulligan', 'Back', 'He', 'For', 'O', 'Christine:', 'Slow', 'Shut', 'One', 'A', 'Silence,', 'He', 'Chrysostomos.', 'Two', 'Thanks,', 'That', 'Switch', 'He', 'The', 'A']
>>> 
>>> #totalList, totalSet
>>> totalList=txt1+txt2
>>> totalSet=set(txt1+txt2)
>>> 
>>> #dictionary
>>> dic={u:len([w for w in totalList if w==u]) for u in totalSet}
>>> dic
{'length,': 1, 'at': 3, 'For': 1, 'do': 1, 'yellow': 1, 'land': 1, 'That': 1, 'middle': 1, 'oval': 1, 'dark': 1, 'rapt': 1, 'here': 1, 'leaned': 1, 'O': 1, 'gold': 1, 'a': 6, 'soul': 1, 'Shut': 1, 'genuine': 1, 'towards': 1, 'briskly.': 1, 'faced': 1, 'shrill': 1, 'beloved,': 1, 'crosses': 1, 'down': 1, 'tone:': 1, 'there': 1, 'all.': 1, 'please.': 1, 'points.': 1, 'gown.': 1, 'round': 1, 'thrice': 1, 'to': 1, 'this,': 1, 'mountains.': 1, 'added': 1, 'will': 2, 'said': 1, 'dearly': 1, 'stairs': 1, 'ages.': 1, 'recalled': 1, 'oak.': 1, 'called': 1, 'that': 1, 'cried': 1, 'hair,': 1, 'with': 1, 'held': 1, 'shaking': 2, 'coarsely:': 1, 'The': 1, 'gravely': 2, 'sternly.': 1, 'about': 3, 'prelate,': 1, 'made': 1, 'lips.': 1, 'under': 1, 'corpuscles.': 1, 'sullen': 1, 'little': 1, 'moment.': 1, 'even': 1, 'Buck': 2, 'body': 1, 'whistles': 1, 'preacher’s': 1, 'patron': 1, 'Dedalus,': 2, 'looked': 2, 'A': 3, 'covered': 1, 'was': 1, 'then': 2, 'glistening': 1, 'quietly': 1, 'whistle': 1, 'current,': 1, 'him': 2, 'displeased': 1, 'Dei.': 1, 'trouble': 1, 'throat': 1, 'intoned:': 1, 'shadowed': 1, 'paused': 1, 'slow': 1, 'mounted': 1, 'Mulligan': 2, 'peered': 2, 'arts': 1, 'equine': 1, 'Two': 1, 'pale': 1, 'sideways': 1, 'he': 5, 'his': 8, 'from': 1, 'its': 1, 'watcher,': 1, 'through': 1, 'gunrest': 1, 'on': 3, 'pleasant': 1, 'awhile': 1, 'strong': 1, 'over': 1, 'those': 1, 'arms': 1, 'altare': 1, 'you': 1, 'jowl': 1, 'nicely.': 1, 'surrounding': 1, 'One': 1, 'call,': 1, 'awaking': 1, 'Halted,': 1, 'smartly.': 1, 'blood': 1, 'old': 1, 'air,': 1, 'your': 1, 'staircase': 1, 'Stately,': 1, 'fearful': 1, 'in': 6, 'Slow': 1, 'Kinch!': 1, 'up': 1, 'morning': 1, 'rapid': 1, 'gurgling': 2, 'stairhead,': 1, 'catching': 1, 'folds': 1, 'hued': 1, 'peeped': 1, 'music,': 1, 'Solemnly': 1, 'attention,': 1, 'Stephen': 2, 'the': 21, 'legs': 1, 'grained': 1, 'blessed': 2, 'Switch': 1, 'smile': 1, 'and': 20, 'calm.': 1, 'gents.': 1, 'Introibo': 1, 'gathering': 1, 'dressinggown,': 1, 'bearing': 1, 'Christine:': 1, 'face': 2, 'aloft': 1, 'mild': 1, 'Come': 2, 'coldly': 1, 'mirror': 2, 'light': 1, 'bent': 1, 'loose': 1, 'long': 1, 'you?': 1, 'air.': 1, 'eyes,': 1, 'white': 2, 'Chrysostomos.': 1, 'sustained': 1, 'ungirdled,': 1, 'lay': 1, 'top': 1, 'chap,': 1, 'is': 1, 'like': 1, 'bowl': 3, 'answered': 1, 'an': 1, 'teeth': 1, 'forward': 1, 'sight': 1, 'jesuit!': 1, 'lather': 1, 'crossed.': 1, 'He': 5, 'out': 1, 'sleepy,': 1, 'instant': 1, 'Back': 1, 'off': 2, 'came': 2, 'skipped': 1, 'untonsured': 1, 'behind': 1, 'him,': 1, 'Thanks,': 1, 'razor': 1, 'gave': 1, 'winding': 1, 'head.': 1, 'broke': 1, 'which': 1, 'barracks!': 1, 'Silence,': 1, 'of': 6, 'Then,': 1, 'plump': 2, 'gunrest.': 1, 'ouns.': 1, 'gently': 1, 'ad': 1, 'up,': 2, 'tower,': 1}
>>> 
>>> #frequency_list
>>> frequency_list=list(dic.values())
>>> frequency_list=sorted(frequency_list)
>>> 
>>> #Answer of No.2
>>> for x in dic:
	if dic[x]==frequency_list[len(frequency_list)-1]:
		print(x)
	elif dic[x]==frequency_list[len(frequency_list)-2]:
		print(x)
	elif dic[x]==frequency_list[len(frequency_list)-3]:
		print(x)

		
his
the
and
>>> 
>>> #set1, set2
>>> set1=set(txt1)
>>> set2=set(txt2)
>>> 
>>> #Answer of No.3
>>> set1.intersection(set2)
{'about', 'at', 'mirror', 'Buck', 'looked', 'A', 'a', 'in', 'bowl', 'Mulligan', 'peered', 'he', 'his', 'He', 'the', 'and', 'of', 'plump', 'gravely', 'face'}
>>> 