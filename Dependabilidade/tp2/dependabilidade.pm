dtmc
	const double RT = 0.97; //0.97
	const double RJSF = 0.98; //0.98
	const double RH = 0.83; //0.83

	const double RM = 0.96; //0.96
	const double RW = 1; //1

module Interface
	si : [0..4] init 0;
	
	[] si=0 -> (RT * 0.1) : (si'=3) + (RT * 0.9) : (si'=1) + (1-RT) : (si'=4); //Tomcat
	[] si=1 -> (RJSF * 0.2) : (si'=3) + (RJSF * 0.8) : (si'=2) + (1-RJSF) : (si'=4); //JSF
	[] si=2 -> (RH) : (si'=3) + (1-RH) : (si'=4); //Hibernate
	[] si=3 -> (si'=3); // estado final de sucesso
	[] si=4 -> (si'=4); // estado final de erro
endmodule

module Collector
	sc : [0..4] init 0;
	
	[] sc=0 -> (RW * 0) : (sc'=3) + (RW * 1) : (sc'=1) + (1-RW) : (sc'=4); //Client
	[] sc=1 -> (RM * 0.6) : (sc'=3) + (RM * 0.4) : (sc'=2) + (1-RM) : (sc'=4); //Server
	[] sc=2 -> (RH) : (sc'=3) + (1-RH) : (sc'=4); //Hibernate
	[] sc=3 -> (sc'=3); // estado final de sucesso
	[] sc=4 -> (sc'=4); // estado final de erro
endmodule