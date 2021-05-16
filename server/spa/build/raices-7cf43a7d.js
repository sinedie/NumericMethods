import{S as e,i as t,s as n,h as a,n as o,B as s,C as l,K as r,o as i,u as $,a as c,D as f,v as u,J as p,x as m,E as d,d as g,y as x,f as b,V as v,j as h,k as w,q as y,r as T,b as k,t as _,p as j,l as z,F as N,G as S,e as F,g as A,c as B}from"./main.js";import{A as C,a as O,S as R,N as D,b as E}from"./SelectItem-0ce85497.js";import{T as P}from"./TextInput-2713e8bc.js";import{D as X}from"./DataTable-1aa59007.js";function G(e){let t,n,b,v,h,w,y,T,k,_,j,z,N,S,F,A=[e[8]],B={};for(let e=0;e<A.length;e+=1)B=a(B,A[e]);return{c(){t=o("div"),n=o("input"),b=s(),v=o("label"),h=l(e[5]),w=s(),y=o("span"),T=o("span"),k=l(e[3]),_=s(),j=o("span"),z=l(e[4]),r(n,"type","checkbox"),n.checked=e[0],n.disabled=e[2],r(n,"id",e[6]),r(n,"name",e[7]),i(n,"bx--toggle-input",!0),i(n,"bx--toggle-input--small","sm"===e[1]),r(T,"aria-hidden","true"),i(T,"bx--toggle__text--off",!0),r(j,"aria-hidden","true"),i(j,"bx--toggle__text--on",!0),i(y,"bx--toggle__switch",!0),r(v,"aria-label",N=e[5]?void 0:e[9]["aria-label"]||"Toggle"),r(v,"for",e[6]),i(v,"bx--toggle-input__label",!0),$(t,B),i(t,"bx--form-item",!0)},m(a,o){c(a,t,o),f(t,n),f(t,b),f(t,v),f(v,h),f(v,w),f(v,y),f(y,T),f(T,k),f(y,_),f(y,j),f(j,z),S||(F=[u(n,"change",e[14]),u(n,"change",e[18]),u(n,"keyup",e[15]),u(n,"keyup",e[19]),u(n,"focus",e[16]),u(n,"blur",e[17]),u(t,"click",e[10]),u(t,"mouseover",e[11]),u(t,"mouseenter",e[12]),u(t,"mouseleave",e[13])],S=!0)},p(e,[a]){1&a&&(n.checked=e[0]),4&a&&(n.disabled=e[2]),64&a&&r(n,"id",e[6]),128&a&&r(n,"name",e[7]),2&a&&i(n,"bx--toggle-input--small","sm"===e[1]),32&a&&p(h,e[5]),8&a&&p(k,e[3]),16&a&&p(z,e[4]),544&a&&N!==(N=e[5]?void 0:e[9]["aria-label"]||"Toggle")&&r(v,"aria-label",N),64&a&&r(v,"for",e[6]),$(t,B=m(A,[256&a&&e[8]])),i(t,"bx--form-item",!0)},i:d,o:d,d(e){e&&g(t),S=!1,x(F)}}}function J(e,t,n){const o=["size","toggled","disabled","labelA","labelB","labelText","id","name"];let s=b(t,o),{size:l="default"}=t,{toggled:r=!1}=t,{disabled:i=!1}=t,{labelA:$="Off"}=t,{labelB:c="On"}=t,{labelText:f=""}=t,{id:u="ccs-"+Math.random().toString(36)}=t,{name:p}=t;const m=v();return e.$$set=e=>{n(9,t=a(a({},t),h(e))),n(8,s=b(t,o)),"size"in e&&n(1,l=e.size),"toggled"in e&&n(0,r=e.toggled),"disabled"in e&&n(2,i=e.disabled),"labelA"in e&&n(3,$=e.labelA),"labelB"in e&&n(4,c=e.labelB),"labelText"in e&&n(5,f=e.labelText),"id"in e&&n(6,u=e.id),"name"in e&&n(7,p=e.name)},e.$$.update=()=>{1&e.$$.dirty&&m("toggle",{toggled:r})},t=h(t),[r,l,i,$,c,f,u,p,s,t,function(t){w(e,t)},function(t){w(e,t)},function(t){w(e,t)},function(t){w(e,t)},function(t){w(e,t)},function(t){w(e,t)},function(t){w(e,t)},function(t){w(e,t)},()=>{n(0,r=!r)},e=>{" "!==e.key&&"Enter"!==e.key||(e.preventDefault(),n(0,r=!r))}]}class M extends e{constructor(e){super(),t(this,e,J,G,n,{size:1,toggled:0,disabled:2,labelA:3,labelB:4,labelText:5,id:6,name:7})}}function I(e){let t,n,a;function o(t){e[16](t)}let s={labelText:"G(x)"};return void 0!==e[1]&&(s.value=e[1]),t=new P({props:s}),z.push((()=>N(t,"value",o))),{c(){y(t.$$.fragment)},m(e,n){T(t,e,n),a=!0},p(e,a){const o={};!n&&2&a&&(n=!0,o.value=e[1],S((()=>n=!1))),t.$set(o)},i(e){a||(k(t.$$.fragment,e),a=!0)},o(e){_(t.$$.fragment,e),a=!1},d(e){j(t,e)}}}function q(e){let t,n,a,o,l,r,i,$,f,u;return t=new E({props:{value:"biseccion",text:"Biseccion"}}),a=new E({props:{value:"punto_fijo",text:"Punto Fijo"}}),l=new E({props:{value:"newton",text:"Newthon Raphson"}}),i=new E({props:{value:"newton_multiple",text:"Newthon Raphson Raices Multiples"}}),f=new E({props:{value:"secante",text:"Secante"}}),{c(){y(t.$$.fragment),n=s(),y(a.$$.fragment),o=s(),y(l.$$.fragment),r=s(),y(i.$$.fragment),$=s(),y(f.$$.fragment)},m(e,s){T(t,e,s),c(e,n,s),T(a,e,s),c(e,o,s),T(l,e,s),c(e,r,s),T(i,e,s),c(e,$,s),T(f,e,s),u=!0},p:d,i(e){u||(k(t.$$.fragment,e),k(a.$$.fragment,e),k(l.$$.fragment,e),k(i.$$.fragment,e),k(f.$$.fragment,e),u=!0)},o(e){_(t.$$.fragment,e),_(a.$$.fragment,e),_(l.$$.fragment,e),_(i.$$.fragment,e),_(f.$$.fragment,e),u=!1},d(e){j(t,e),e&&g(n),j(a,e),e&&g(o),j(l,e),e&&g(r),j(i,e),e&&g($),j(f,e)}}}function K(e){let t,n,a,o;return t=new E({props:{value:"abs",text:"Absoluto"}}),a=new E({props:{value:"rel",text:"Relativo"}}),{c(){y(t.$$.fragment),n=s(),y(a.$$.fragment)},m(e,s){T(t,e,s),c(e,n,s),T(a,e,s),o=!0},p:d,i(e){o||(k(t.$$.fragment,e),k(a.$$.fragment,e),o=!0)},o(e){_(t.$$.fragment,e),_(a.$$.fragment,e),o=!1},d(e){j(t,e),e&&g(n),j(a,e)}}}function U(e){let t,n,a;function o(t){e[23](t)}let s={labelText:"Usar regla falsa"};return void 0!==e[7]&&(s.toggled=e[7]),t=new M({props:s}),z.push((()=>N(t,"toggled",o))),{c(){y(t.$$.fragment)},m(e,n){T(t,e,n),a=!0},p(e,a){const o={};!n&&128&a&&(n=!0,o.toggled=e[7],S((()=>n=!1))),t.$set(o)},i(e){a||(k(t.$$.fragment,e),a=!0)},o(e){_(t.$$.fragment,e),a=!1},d(e){j(t,e)}}}function V(e){let t,n,a,o,l,r,i,$,f,u,p,m,d,x,b,v,h,w,C,O,E,X,G,J;function M(t){e[15](t)}let V={labelText:"Funcion"};void 0!==e[0]&&(V.value=e[0]),t=new P({props:V}),z.push((()=>N(t,"value",M)));let H="punto_fijo"==e[2]&&I(e);function L(t){e[17](t)}let Q={labelText:"Metodo",$$slots:{default:[q]},$$scope:{ctx:e}};function W(t){e[18](t)}void 0!==e[2]&&(Q.selected=e[2]),l=new R({props:Q}),z.push((()=>N(l,"selected",L)));let Y={labelText:"Tipo de error",$$slots:{default:[K]},$$scope:{ctx:e}};function Z(t){e[19](t)}void 0!==e[6]&&(Y.selected=e[6]),$=new R({props:Y}),z.push((()=>N($,"selected",W)));let ee={label:"Coordenada inicial del intervalo"};function te(t){e[20](t)}void 0!==e[3]&&(ee.value=e[3]),p=new D({props:ee}),z.push((()=>N(p,"value",Z)));let ne={label:"Coordenada final del intervalo"};function ae(t){e[21](t)}void 0!==e[4]&&(ne.value=e[4]),x=new D({props:ne}),z.push((()=>N(x,"value",te)));let oe={label:"Tolerancia",positive:!0};function se(t){e[22](t)}void 0!==e[5]&&(oe.value=e[5]),h=new D({props:oe}),z.push((()=>N(h,"value",ae)));let le={label:"Numero maximo de iteraciones",integer:!0,positive:!0};void 0!==e[8]&&(le.value=e[8]),O=new D({props:le}),z.push((()=>N(O,"value",se)));let re="biseccion"==e[2]&&U(e);return{c(){y(t.$$.fragment),a=s(),H&&H.c(),o=s(),y(l.$$.fragment),i=s(),y($.$$.fragment),u=s(),y(p.$$.fragment),d=s(),y(x.$$.fragment),v=s(),y(h.$$.fragment),C=s(),y(O.$$.fragment),X=s(),re&&re.c(),G=F()},m(e,n){T(t,e,n),c(e,a,n),H&&H.m(e,n),c(e,o,n),T(l,e,n),c(e,i,n),T($,e,n),c(e,u,n),T(p,e,n),c(e,d,n),T(x,e,n),c(e,v,n),T(h,e,n),c(e,C,n),T(O,e,n),c(e,X,n),re&&re.m(e,n),c(e,G,n),J=!0},p(e,a){const s={};!n&&1&a&&(n=!0,s.value=e[0],S((()=>n=!1))),t.$set(s),"punto_fijo"==e[2]?H?(H.p(e,a),4&a&&k(H,1)):(H=I(e),H.c(),k(H,1),H.m(o.parentNode,o)):H&&(A(),_(H,1,1,(()=>{H=null})),B());const i={};268435456&a&&(i.$$scope={dirty:a,ctx:e}),!r&&4&a&&(r=!0,i.selected=e[2],S((()=>r=!1))),l.$set(i);const c={};268435456&a&&(c.$$scope={dirty:a,ctx:e}),!f&&64&a&&(f=!0,c.selected=e[6],S((()=>f=!1))),$.$set(c);const u={};!m&&8&a&&(m=!0,u.value=e[3],S((()=>m=!1))),p.$set(u);const d={};!b&&16&a&&(b=!0,d.value=e[4],S((()=>b=!1))),x.$set(d);const g={};!w&&32&a&&(w=!0,g.value=e[5],S((()=>w=!1))),h.$set(g);const v={};!E&&256&a&&(E=!0,v.value=e[8],S((()=>E=!1))),O.$set(v),"biseccion"==e[2]?re?(re.p(e,a),4&a&&k(re,1)):(re=U(e),re.c(),k(re,1),re.m(G.parentNode,G)):re&&(A(),_(re,1,1,(()=>{re=null})),B())},i(e){J||(k(t.$$.fragment,e),k(H),k(l.$$.fragment,e),k($.$$.fragment,e),k(p.$$.fragment,e),k(x.$$.fragment,e),k(h.$$.fragment,e),k(O.$$.fragment,e),k(re),J=!0)},o(e){_(t.$$.fragment,e),_(H),_(l.$$.fragment,e),_($.$$.fragment,e),_(p.$$.fragment,e),_(x.$$.fragment,e),_(h.$$.fragment,e),_(O.$$.fragment,e),_(re),J=!1},d(e){j(t,e),e&&g(a),H&&H.d(e),e&&g(o),j(l,e),e&&g(i),j($,e),e&&g(u),j(p,e),e&&g(d),j(x,e),e&&g(v),j(h,e),e&&g(C),j(O,e),e&&g(X),re&&re.d(e),e&&g(G)}}}function H(e){let t,n,a,s,r;return{c(){t=o("h2"),n=l("Raiz: "),a=l(e[12]),s=l("\n    Notas: "),r=l(e[11])},m(e,o){c(e,t,o),f(t,n),f(t,a),c(e,s,o),c(e,r,o)},p(e,t){4096&t&&p(a,e[12]),2048&t&&p(r,e[11])},d(e){e&&g(t),e&&g(s),e&&g(r)}}}function L(e){let t,n,a,l,i,$,f,u,p;function m(t){e[24](t)}let d={label:"Coordenada inicial"};function x(t){e[25](t)}void 0!==e[9]&&(d.value=e[9]),l=new D({props:d}),z.push((()=>N(l,"value",m)));let b={label:"Coordenada final"};return void 0!==e[10]&&(b.value=e[10]),f=new D({props:b}),z.push((()=>N(f,"value",x))),{c(){t=o("img"),a=s(),y(l.$$.fragment),$=s(),y(f.$$.fragment),t.src!==(n=e[14])&&r(t,"src",n),r(t,"alt","Representacion grafica de la funcion")},m(e,n){c(e,t,n),c(e,a,n),T(l,e,n),c(e,$,n),T(f,e,n),p=!0},p(e,a){(!p||16384&a&&t.src!==(n=e[14]))&&r(t,"src",n);const o={};!i&&512&a&&(i=!0,o.value=e[9],S((()=>i=!1))),l.$set(o);const s={};!u&&1024&a&&(u=!0,s.value=e[10],S((()=>u=!1))),f.$set(s)},i(e){p||(k(l.$$.fragment,e),k(f.$$.fragment,e),p=!0)},o(e){_(l.$$.fragment,e),_(f.$$.fragment,e),p=!1},d(e){e&&g(t),e&&g(a),j(l,e),e&&g($),j(f,e)}}}function Q(e){let t,n;return t=new X({props:{headers:[{key:"id",value:"i"},{key:"x",value:"X(i)"},{key:"fx",value:"F( X(i) )"},{key:"err",value:`Error ${e[6]}`}],rows:e[13]}}),{c(){y(t.$$.fragment)},m(e,a){T(t,e,a),n=!0},p(e,n){const a={};64&n&&(a.headers=[{key:"id",value:"i"},{key:"x",value:"X(i)"},{key:"fx",value:"F( X(i) )"},{key:"err",value:`Error ${e[6]}`}]),8192&n&&(a.rows=e[13]),t.$set(a)},i(e){n||(k(t.$$.fragment,e),n=!0)},o(e){_(t.$$.fragment,e),n=!1},d(e){j(t,e)}}}function W(e){let t,n,a,o,l,r,i,$;return t=new O({props:{title:"Opciones",open:!0,$$slots:{default:[V]},$$scope:{ctx:e}}}),a=new O({props:{title:"Raiz",open:!0,$$slots:{default:[H]},$$scope:{ctx:e}}}),l=new O({props:{title:"Grafica",open:!0,$$slots:{default:[L]},$$scope:{ctx:e}}}),i=new O({props:{title:"Procedimiento",$$slots:{default:[Q]},$$scope:{ctx:e}}}),{c(){y(t.$$.fragment),n=s(),y(a.$$.fragment),o=s(),y(l.$$.fragment),r=s(),y(i.$$.fragment)},m(e,s){T(t,e,s),c(e,n,s),T(a,e,s),c(e,o,s),T(l,e,s),c(e,r,s),T(i,e,s),$=!0},p(e,n){const o={};268435967&n&&(o.$$scope={dirty:n,ctx:e}),t.$set(o);const s={};268441600&n&&(s.$$scope={dirty:n,ctx:e}),a.$set(s);const r={};268453376&n&&(r.$$scope={dirty:n,ctx:e}),l.$set(r);const $={};268443712&n&&($.$$scope={dirty:n,ctx:e}),i.$set($)},i(e){$||(k(t.$$.fragment,e),k(a.$$.fragment,e),k(l.$$.fragment,e),k(i.$$.fragment,e),$=!0)},o(e){_(t.$$.fragment,e),_(a.$$.fragment,e),_(l.$$.fragment,e),_(i.$$.fragment,e),$=!1},d(e){j(t,e),e&&g(n),j(a,e),e&&g(o),j(l,e),e&&g(r),j(i,e)}}}function Y(e){let t,n;return t=new C({props:{$$slots:{default:[W]},$$scope:{ctx:e}}}),{c(){y(t.$$.fragment)},m(e,a){T(t,e,a),n=!0},p(e,[n]){const a={};268468223&n&&(a.$$scope={dirty:n,ctx:e}),t.$set(a)},i(e){n||(k(t.$$.fragment,e),n=!0)},o(e){_(t.$$.fragment,e),n=!1},d(e){j(t,e)}}}function Z(e,t,n){let a,o,s,l="x + 100",r="100",i="biseccion",$=-200,c=100,f=1e-6,u="abs",p=!1,m=1e3,d=[],g=-200,x=0;return e.$$.update=()=>{511&e.$$.dirty&&async function(){try{const e=await fetch(`/api/raices/${i}`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({xi:$,xf:c,tol:f,err:u,n_max_iter:m,func:l,func_g:r,regla_falsa:p,multiplicidad_raiz:1})}),t=await e.json();n(12,o=t.raiz[0]),n(11,a=t.raiz[1]),n(13,d=t.raiz[2].map(((e,t)=>({id:t,x:e[0].toFixed(10),fx:e[1].toFixed(10),err:e[2].toFixed(10)}))))}catch{}}(),1537&e.$$.dirty&&(l||g||x)&&async function(){try{const e=await fetch("/api/raices/grafico",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({func:l,xi:g,xf:x})}),t=await e.json();n(14,s=`data:image/jpeg;base64, ${t.image}`)}catch(e){console.log(e)}}()},[l,r,i,$,c,f,u,p,m,g,x,a,o,d,s,function(e){l=e,n(0,l)},function(e){r=e,n(1,r)},function(e){i=e,n(2,i)},function(e){u=e,n(6,u)},function(e){$=e,n(3,$)},function(e){c=e,n(4,c)},function(e){f=e,n(5,f)},function(e){m=e,n(8,m)},function(e){p=e,n(7,p)},function(e){g=e,n(9,g)},function(e){x=e,n(10,x)}]}export default class extends e{constructor(e){super(),t(this,e,Z,Y,n,{})}}
//# sourceMappingURL=raices-7cf43a7d.js.map