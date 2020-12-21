% ---Matlab Code---

%User's inputs

h = input("Please enter the step length: ");
X0 = input("Please Enter the initial value of X: ");
Y0 = input("Please enter the initial value of Y:");

X = input("Please enter the desired value of X to find the value of Y(X): ");

% -------------------------------------------------------------------------------
%Holds the X and Y to not change the original inputs

a = X0;
b = Y0;

% -------------------------------------------------------------------------------
% Testing
F = equation(a,b);
disp(F)

% -------------------------------------------------------------------------------

% Method one to approaching the task
%         Yn = Yn-1 + 0.5(K1 + K2)
%             Where:
%                 K1 = hf(Xn-1, Yn-1)
%                 K2 = hf(Xn-1 + h, Yn-1 + K1)


for i = 0: h : X-h
    K1 = h*equation(a,b);
    disp (newline +"K1 = " + K1);
    K2 = h*equation(a+h,b+K1);
    disp ("K2 = " + K2);
    Yn = b + 0.5*(K1 + K2);
    a = a + h;
    j = a;
    disp (newline + "Y("+ j + ") =" + Yn);
    b = Yn;
    disp ("The new X = "+ a + " and new Y = " + b);
end

% -------------------------------------------------------------------------------

% Method two to approaching the task
%         Yn = Yn-1 + K2
%             Where:
%                 K2 = hf(Xn-1 + h/2, Yn-1 + K1/2)
%                 K1 = hf(Xn-1, Yn-1)

% for i = 0: h : X-h
%     K1 = h*equation(a,b);
%     disp (newline +"K1 = " + K1);
%     K2 = h*equation(a+h/2,b+K1/2);
%     disp ("K2 = " + K2);
%     Yn = b + K2;
%     a = a + h;
%     j = a;
%     disp (newline + "Y("+ j + ") =" + Yn);
%     b = Yn;
%     disp ("The new X = "+ a + " and new Y = " + b);
% end
% -------------------------------------------------------------------------------

% Here is the function calculation

function F = equation(x,y)
%     This is the equation
    F = (x - y)/2;
%     Change Equation to any other desired equation
end