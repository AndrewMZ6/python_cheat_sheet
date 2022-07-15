from threading import Thread
from func_module import my_gen

L = []

def thr1():
	for i in my_gen(30):
		L.append(f"t1::{i}")
	print("thread 1 done!")

def thr2():
	for j in my_gen(30):
		L.append(f"t2::{j}")
	print("thread 2 done!")

def main_thr():
	for k in my_gen(40):
		L.append(f"mt::{k}")
	print("main thread done!")

t1 = Thread(target=thr1)
t2 = Thread(target=thr2)

t1.start()
t2.start()
main_thr()

print(len(L))

# output:
thread 1 done!
# thread 2 done!
# main thread done!
# 100
# mt::blackautumn@example.net
# t1::pacechristina@example.org
# t2::mbradley@example.net
# mt::kevin01@example.net
# t1::robinyoung@example.com
# t2::brownjason@example.net
# mt::velasquezkristin@example.org
# t2::rachel04@example.net
# t1::vanderson@example.com
# mt::darrell61@example.com
# t2::brooke69@example.com
# t1::xcarter@example.com
# mt::ugonzales@example.net
# t1::james57@example.org
# t2::adamcarter@example.com
# mt::bsmith@example.net
# t1::dpatrick@example.net
# t2::cody52@example.org
# t1::victoria34@example.net
# mt::zsalas@example.com
# t2::jgriffin@example.com
# mt::danajohnson@example.com
# t1::gibbstracy@example.net
# t2::brittneymaxwell@example.net
# mt::reynoldslaura@example.net
# t1::natasha60@example.com
# t2::uritter@example.net
# mt::wsmith@example.com
# t1::rmartin@example.com
# t2::mrivera@example.net
# mt::vrivera@example.net
# t1::kimberlyking@example.org
# t2::katrinafuller@example.org
# mt::kimashley@example.net
# t1::christian14@example.com
# t2::benjamin74@example.org
# mt::brownsarah@example.net
# t1::kwallace@example.com
# t2::tuckersuzanne@example.com
# mt::wintersnicole@example.com
# t1::andersonscott@example.net
# t2::dustingrimes@example.org
# mt::ozimmerman@example.net
# t1::stephanie65@example.com
# t2::peggycole@example.org
# mt::jacobtaylor@example.org
# t1::christina19@example.com
# t2::holly69@example.net
# mt::cory64@example.net
# t1::varnold@example.net
# t2::lnichols@example.net
# mt::floydcarrie@example.net
# t1::stephen54@example.net
# t2::patriciagreene@example.org
# mt::tamara53@example.org
# t1::hayley16@example.com
# t2::ianwheeler@example.org
# mt::hgallagher@example.com
# t1::victoria00@example.net
# t2::whiterobert@example.net
# mt::david51@example.com
# t1::haynesmichelle@example.com
# t2::brettreid@example.com
# mt::martinezsamantha@example.com
# t1::nhendricks@example.com
# t2::sdavis@example.com
# mt::abean@example.org
# t1::lsmith@example.org
# t2::michaellambert@example.com
# mt::juan80@example.org
# t1::bruce70@example.org
# t2::derek83@example.net
# mt::jeffreygardner@example.org
# t1::apham@example.net
# t2::morenocaroline@example.net
# mt::tbaker@example.com
# t1::chase90@example.org
# t2::randy96@example.com
# t1::shane14@example.com
# mt::princetyler@example.com
# t2::adamsclaudia@example.com
# mt::randerson@example.net
# t1::burchlindsay@example.com
# t2::dwyatt@example.net
# mt::edwardjackson@example.org
# t1::jeremiah36@example.com
# t2::david86@example.org
# mt::elizabethboyd@example.net
# t1::katie52@example.org
# t2::thomas59@example.net
# mt::joshua76@example.net
# mt::jameswalters@example.com
# mt::kayla01@example.com
# mt::sallyfuller@example.net
# mt::lsimpson@example.com
# mt::stewartraven@example.net
# mt::dunnsheri@example.org
# mt::travis10@example.net
# mt::mmiller@example.com
# mt::ronaldbrown@example.org
# [Finished in 7.2s]
