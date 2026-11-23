// Datebell site: language, App Store campaign links, small motion. Shared by index.html and features.html.
(function(){
  var d=document,q=new URLSearchParams(location.search);
  var APP='6821503223',PT='129594804';
  var ct=(q.get('ct')||'').trim();
  if(/^[A-Za-z0-9._-]{1,40}$/.test(ct)){
    var href='https://apps.apple.com/app/apple-store/id'+APP+'?pt='+PT+'&ct='+encodeURIComponent(ct)+'&mt=8';
    d.querySelectorAll('a.store').forEach(function(a){a.href=href;});
  }else ct='';
  // keep ?ct and ?lang when moving between Home and Features
  d.querySelectorAll('a.keepq').forEach(function(a){
    var u=a.getAttribute('href'),h='';var i=u.indexOf('#');if(i>=0){h=u.slice(i);u=u.slice(0,i);}
    var p=new URLSearchParams();if(ct)p.set('ct',ct);if(q.get('lang'))p.set('lang',q.get('lang'));
    var s=p.toString();a.setAttribute('href',u+(s?'?'+s:'')+h);
  });
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;

  var BADGE={th:'https://tools.applemarketingtools.com/api/badges/download-on-the-app-store/black/th-th',en:'img/badge-en.svg'};
  var BADGE_ALT={th:'ดาวน์โหลดบน App Store',en:'Download on the App Store'};
  var TITLE=window.DB_TITLE||{th:'Datebell',en:'Datebell'};
  var lang,hooks=[];
  function setLang(l){
    lang=l;d.documentElement.lang=l;d.title=TITLE[l];
    try{localStorage.setItem('db-lang',l);}catch(e){}
    d.querySelectorAll('.lang button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.set===l?'true':'false');});
    d.querySelectorAll('img[data-src]').forEach(function(im){im.src=im.dataset.src.replace('{l}',l);});
    d.querySelectorAll('img.badgeImg').forEach(function(b){b.onerror=function(){b.onerror=null;b.src=BADGE.en;};b.src=BADGE[l];b.alt=BADGE_ALT[l];});
    hooks.forEach(function(f){f(l);});
  }
  d.querySelectorAll('.lang button').forEach(function(b){b.onclick=function(){setLang(b.dataset.set);};});
  var saved=null;try{saved=localStorage.getItem('db-lang');}catch(e){}
  var start=q.get('lang')==='en'||q.get('lang')==='th'?q.get('lang')
    :/-th-|^th-|-th$/.test(ct)?'th'
    :/-(gl|en)-|-(gl|en)$/.test(ct)?'en'
    :saved||(/^th\b/i.test(navigator.language||'')?'th':(ct?'th':'en'));

  // home: real Simulator walkthrough (Bobby-style), image stays until the video plays
  var walk=d.getElementById('walk');
  if(walk&&!reduce){
    walk.addEventListener('playing',function(){walk.classList.add('on');});
    hooks.push(function(l){var src='video/walkthrough-'+l+'.mp4';if(walk.getAttribute('src')===src)return;walk.classList.remove('on');walk.src=src;var p=walk.play();if(p&&p.catch)p.catch(function(){});});
  }
  var ntf=d.getElementById('ntf');
  if(ntf){
    function dfmt(l,days,year){var x=new Date();x.setDate(x.getDate()+days);var o={day:'numeric',month:'short'};if(year)o.year='numeric';return new Intl.DateTimeFormat(l==='th'?'th-TH':'en-US',o).format(x);}
    function list(l){return l==='th'
      ?[['ทดลองใช้ฟรีหมดในอีก 2 วัน','ทดลองใช้ฟรี YouTube Premium หมด '+dfmt(l,2)+' ถ้าไม่ใช้ต่อ ยกเลิกล่วงหน้าอย่างน้อย 1 วัน'],['ใกล้ถึงกำหนด','Spotify · ตัดเงินพรุ่งนี้ '+dfmt(l,1)],['ใกล้ถึงกำหนด','พาสปอร์ต · หมดอายุ '+dfmt(l,180,1)]]
      :[['Free trial ends in 2 days','Your Disney+ free trial ends '+dfmt(l,2)+'. Cancel at least a day before if you don’t want to pay.'],['Due soon','Spotify · Payment tomorrow, '+dfmt(l,1)],['Due soon','Passport · Expires '+dfmt(l,180,1)]];}
    var nk=0,NOW={th:'ตอนนี้',en:'now'};
    function set(){var n=list(lang)[nk%3];d.getElementById('ntfTitle').textContent='Datebell · '+n[0];d.getElementById('ntfText').textContent=n[1];d.getElementById('ntfTime').textContent=NOW[lang];}
    hooks.push(set);
    if(reduce){ntf.classList.add('on');}
    else{
      setTimeout(function(){ntf.classList.add('on');},1200);
      setInterval(function(){if(d.hidden)return;ntf.classList.remove('on');setTimeout(function(){nk++;set();ntf.classList.add('on');},600);},4200);
    }
  }

  // features: theme picker cycles until the visitor picks one
  var tv=d.getElementById('themeVis');
  if(tv){
    var btns=d.querySelectorAll('#themeSw button'),ti=tv.querySelectorAll('.stack img'),order=['auto','lemon','cloud','cocoa'],t=0,tAuto=!reduce,seenT=false;
    function setT(x){tv.dataset.t=x;t=order.indexOf(x);btns.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.t===x?'true':'false');});ti.forEach(function(im){im.classList.toggle('on',im.dataset.t===x);});}
    btns.forEach(function(b){b.onclick=function(){tAuto=false;setT(b.dataset.t);};});
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){seenT=es[0].isIntersecting;}).observe(tv);
    setInterval(function(){if(!tAuto||!seenT||d.hidden)return;setT(order[(t+1)%order.length]);},2600);
  }

  setLang(start);

  // reveal on scroll
  var rv=d.querySelectorAll('.rv');
  if(('IntersectionObserver' in window)&&!reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -10% 0px'});
    rv.forEach(function(el){io.observe(el);});
  }else rv.forEach(function(el){el.classList.add('in');});
})();
