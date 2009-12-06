dtmc
	const double RJSF = 0.99;
	const double RT = 0.99;
	const double RH = 0.99;

	const double RS = 0.99;
	const double RC = 0.99;

module Interface
	si : [0..4] init 0;
	
	[] si=0 -> (RJSF * 0.2) : (si'=3) + (RJSF * 0.8) : (si'=1) + (1-RJSF) : (si'=4); //JSF
	[] si=1 -> (RT * 0.1) : (si'=3) + (RT * 0.9) : (si'=2) + (1-RT) : (si'=4); //Tomcat
	[] si=2 -> (RH) : (si'=3) + (1-RH) : (si'=4); //Hibernate
	[] si=3 -> (si'=3); // estado final de sucesso
	[] si=4 -> (si'=4); // estado final de erro
endmodule

module Collector
	sc : [0..4] init 0;
	
	[] sc=0 -> (RC * 0) : (sc'=3) + (RC * 1) : (sc'=1) + (1-RC) : (sc'=4); //Client
	[] sc=1 -> (RS * 0.6) : (sc'=3) + (RS * 0.4) : (sc'=2) + (1-RS) : (sc'=4); //Server
	[] sc=2 -> (RH) : (sc'=3) + (1-RH) : (sc'=4); //Hibernate
	[] sc=3 -> (sc'=3); // estado final de sucesso
	[] sc=4 -> (sc'=4); // estado final de erro
endmodule