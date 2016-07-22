% SPA  Lecture CODES:
% Jun. 2016
% by G.G.
%% WEEK 3
M = 1000;
n = 0:M-1; %1000 samples
x = exp(j*0.02*pi*n);
fft_of_x = fft(x);

k = [0:M/2 (-M/2+1):-1];
plot(k,abs(fft_of_x))
title('Without frequency labeling')
xlabel('bins')
axis([-550 550 -50 1200])
% xlim( [-100 100])

figure;
fs=500;
f = k*fs/1000; % k*fs/M
plot(f,abs(fft(x)))
title('With frequency labeling');
xlabel('Frequency - Hz');
axis([-300 300 -50 1200])
xlim([-30 30])

%
fs=2000;
n = 0:2*fs-1;

x = sin(0.25*pi*n)+cos(0.1*pi*n)+0.5;
t = n/fs;
subplot(3,1,1)
plot(t,sin(0.25*pi*n));ylim([-2 2]);
title('Sin. component');
subplot(3,1,2)
plot(t,cos(0.1*pi*n));ylim([-2 2])
title('Cos. component');
subplot(3,1,3)
plot(t,x);ylim([-4 4])
xlabel('Time - seconds');
figure
M=1000;
k = [0:M/2 -M/2+1:-1];
plot(k,abs(fft(x,M)))
xlabel('FFT bins');

fr = k*fs/M;
figure
plot(fr,abs(fft(x,M)));
xlabel('Frequency (Hz)')
xlim([-400 400])
figure
plot(fr,abs(fft(x,M))/M);
xlabel('Frequency (Hz)')
xlim([-400 400])

x=x+1.5
figure
plot(fr,abs(fft(x,M))/M);
xlabel('Frequency (Hz)')
xlim([-400 400])
ylim([0 2.2])

%% WEEK 5

fs = 100;
n=0:fs-1; % 100 samples
M=length(n);
t=n/fs;
x1 = sin(20*pi*t);
x2 = sin(20*pi*t.^2);

k = [0:M/2 -M/2+1:-1];
plot(k*fs/M,abs(fft(x1))/M)
hold on
plot(k*fs/M,abs(fft(x2))/M,'r')
xlabel('Frequency (Hz');

% 
fs=100;
n=0:10*fs-1;
M=length(n);
t=n/fs;
x = sin(2*pi*t.^2 + 10*pi*t)
figure
plot(t,x)
title('x(t)=sin(2\pit^2 + 10\pit)')
k=[0:M/2 -M/2+1:-1]
figure
plot(k*fs/M,abs(fft(x))/M)
title('FFT of x');
xlabel('Frequency (Hz)')
%%
xwin = buffer(x,100,50,'nodelay');
sfftx = fft(xwin)/100; 
k = [0:50 -49:-1]
subplot(3,1,1);
plot(k,abs(sfftx(:,1)))
title('FFT of window 1')
subplot(3,1,2);
plot(k,abs(sfftx(:,10)))
title('FFT of window 10')
subplot(3,1,3);
plot(k,abs(sfftx(:,19)))
title('FFT of window 19')
xlabel('FFT bins')
figure
mesh(1:19,k,abs(sfftx))
xlabel('Window Index');
ylabel('FFT bins')

figure
surf(1:19,k,abs(sfftx))
xlabel('Window Index');
ylabel('FFT bins')
shading interp
%% 
% WEEK 6
M=40;
n=0:M-1;
x= cos(pi*n)
k = [0:M/2 -M/2+1:-1];
plot(k,abs(fft(x))/M,'.')
hold on
plot(k,abs(fft(x))/M,'or')
grid; ylim([0 1.25]);
xlim([-21 21])
xlabel('FFT bins');
figure
plot(k*100/M,abs(fft(x))/M,'or')
grid; ylim([0 1.25]);
xlabel('Frequency (Hz)');
xlim([-55 55])
% Example 4

fs = 8000;
n = 0:4*fs-1;
t = n/fs;
phasex = 2*pi*1000*(t.^2) + 4*pi*1000*t;
x = sin(phasex);
xwin = buffer(x,.125*fs,.125*fs*.5,'nodelay');
mesh(abs(fft(xwin))/1000);
shading interp
xlabel('Window indeces');
ylabel('FFT bin indices');
axis tight

figure
[Nk Nwin]=size(xwin);% row and column
fr_win=[0:Nk/2 -Nk/2+1:-1]*fs/Nk; % for row ticks
win_ticks=linspace(0,4,Nwin); % for column ticks

mesh(win_ticks, fr_win, abs(fft(xwin))/Nk);
shading interp;
xlabel('Time (sec)');%column label
ylabel('Frequency (Hz)');%row label

