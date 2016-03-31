initTimes = [0.000163707,0.000622905,0.00141165,0.00249452,0.00388239,0.0061674,0.00806767,0.0107595,0.0128599,0.0161829,0.0191738,0.0233933,0.026332,0.031127,0.0365778,0.0408588,0.0481683,0.0501633,0.0568939,0.0662243,0.0711,0.0767107,0.0883953,0.100316,0.10119];
invTimes = [0.000217716,0.00167448,0.00552115,0.0129649,0.0257418,0.0441518,0.0737702,0.103916,0.152754,0.2005,0.265786,0.348179,0.443567,0.556201,0.684578,0.82684,0.989027,1.18225,1.38899,1.6143,1.96093,2.18813,2.5337,2.89806,3.22259];

initTimes1 = [0.000156961,0.000630752,0.00144904,0.00251847,0.00391062,0.00564136,0.00770673,0.0101543,0.0125661,0.0155184,0.0187237,0.0233851,0.0268171,0.0317651,0.0345551,0.0394702,0.0449627,0.0521596,0.0565906,0.06272,0.0696411,0.0771784,0.0861619,0.0909864,0.0985745];
invTimes1 = [0.000216895,0.00166426,0.00545052,0.0126793,0.0246595,0.0423399,0.066771,0.0987089,0.141166,0.192546,0.264384,0.365301,0.443902,0.538941,0.638024,0.77128,0.932359,1.10385,1.29988,1.55833,1.74649,2.00708,2.2906,2.61726,2.98092];

invCoeff = polyfit(20:20:500,initTimes + invTimes,3);

% for ax^3 + bx^2 :
b = invCoeff(2);
a = invCoeff(1);

figure
subplot(1,2,1);
scatter(20:20:500,initTimes + invTimes);
hold on;
scatter(20:20:500, a*(20:20:500).^3 + b*(20:20:500).^2, '+');
 title('Matrix Inversion');
    ylabel('Time (s)')
    xlabel(['Matrix Size (NxN) A=' num2str(a) ' B=' num2str(b)]);
    legend('Measured','Predicted')
   
    subplot(1,2,2);
    errors = bsxfun(@rdivide,(abs((a*(20:20:500).^3 + b*(20:20:500).^2)) - (initTimes + invTimes)),(initTimes + invTimes));
    scatter(20:20:500, errors);
    hold on;
    p1 = [0,0];
    p2 = [0,500];
    plot([p1(2),p2(2)],[p1(1),p2(1)],'Color','b','LineWidth',1);
    title('Matrix Inversion Model Error');
    ylabel('Error Proportion')
    xlabel('Matrix Size (NxN)');
    