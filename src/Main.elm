module Main exposing (main)

import Browser exposing (document)
import Browser.Events
import Element exposing (Element, column, el, height, px, text, width)
import Element.Font as Font
import Html exposing (Html)
import Mark.Error
import Markup exposing (Day)
import Task


main : Program Flags Model Msg
main =
    document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }



-- MODEL


type alias Model =
    { size : WindowSize
    , markup : String
    }


type alias WindowSize =
    { width : Int
    , height : Int
    }


type alias Flags =
    { size : WindowSize
    , markup : String
    }


type Msg
    = SetSize WindowSize



-- INIT


init : Flags -> ( Model, Cmd Msg )
init { size, markup } =
    ( { size = size
      , markup = markup
      }
    , Cmd.none
    )



-- UPDATE


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetSize size ->
            ( { model | size = size }, Cmd.none )



-- VIEW


view : Model -> Browser.Document Msg
view model =
    { title = ""
    , body = [ Element.layout [] (body model) ]
    }


type Layout
    = Wide
    | Narrow


body : Model -> Element Msg
body model =
    let
        layout =
            if toFloat model.size.width / toFloat model.size.height > 1.3 then
                Wide

            else
                Narrow
    in
    case Markup.parseDocument model.markup of
        Ok days ->
            column [ Element.centerX ] (List.map (dayElement layout) days)

        Err [] ->
            Element.text "There were errors but there are no errors..."

        Err (firstError :: _) ->
            Element.text (Debug.toString <| Mark.Error.toDetails firstError)


dayElement : Layout -> Day Msg -> Element Msg
dayElement layout day =
    let
        title_ =
            dayTitle day.day day.name

        image_ =
            image day.currentImage
    in
    case layout of
        Narrow ->
            Element.column []
                [ title_
                , day.description
                , image_
                ]

        Wide ->
            Element.row []
                [ image_
                , Element.column []
                    [ title_
                    , day.description
                    ]
                ]


dayTitle : Int -> String -> Element Msg
dayTitle day title_ =
    el [ Element.onLeft (title (String.fromInt day ++ ". ")) ] (title title_)


title : String -> Element Msg
title string =
    el [ Font.size 24, Font.bold ] (text string)


image : String -> Element Msg
image src =
    Element.image [ width (px 500), height (px 500) ]
        { src = src, description = "" }



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions model =
    Browser.Events.onResize (\wd ht -> SetSize { width = wd, height = ht })
