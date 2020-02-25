module display_decoder(
    input  wire clk,
   input wire A,
 input wire B,
input wire C,
input wire D,
    output reg a,
    output reg b,
    output reg c,
    output reg d,
);

  always @(posedge clk) begin
  
  a=A;
  b=B;
  c=C;
  d=D;
  
       
 end

endmodule